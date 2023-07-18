from fabric.tasks import task
import time
import re
import os
import csv
import matplotlib.pyplot as plt

from local import LocalBench
from utils import Print, BenchError, PathMaker
from plots import plot_metric


csv_directory = "./results/csv"
log_directory = "./results/logs"

config = {
    # Faults vs Latency | Faults vs Throughput | Throughput vs Latency
    1: {
        'faults': [0, 1, 2, 3, 4],
        'nodes': [10],
        'rate': [1_687],
        'tx_size': [512],
        'runs': 10
    },
    # Nodes vs Latency | Nodes vs Throughput | Throughput vs Latency
    2: {
        'faults': [0],
        'nodes': [10, 20, 30, 40],
        'rate': [1_687],
        'tx_size': [512],
        'runs': 10
    },
    # Tx size vs Latency | Tx size vs Throughput | Throughput vs Latency
    3: {
        'faults': [0],
        'nodes': [10],
        'rate': [1_687],
        'tx_size': [128, 256, 512, 1_024, 2_048],
        'runs': 10
    },
    # Unión de las tres anteriores con aumentos de TPS
    4: {
        'faults': [0, 1, 2, 3, 4],
        'nodes': [10, 20, 30, 40],
        'rate': [1_687, 3000, 4000, 5000],
        'tx_size': [128, 256, 512, 1_024, 2_048],
        'runs': 10
    },
}


@task
def local(ctx):
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    for config_id, params in config.items():
        faults = params['faults']
        nodes = params['nodes']
        rate = params['rate']
        tx_size = params['tx_size']
        runs = params['runs']

        ''' Run benchmarks on localhost '''
        for fault in faults:
            for node in nodes:
                for r in rate:
                    for size in tx_size:
                        bench_params = {
                            'faults': fault,
                            'nodes': node,
                            'rate': r,
                            'tx_size': size,
                            'duration': 10,  # 60 segundos
                            'runs': runs
                        }
                        node_params = {
                            'consensus': {
                                'timeout_delay': 5_000,  # ms
                                'sync_retry_delay': 5_000,  # ms
                            },
                            'mempool': {
                                'gc_depth': 50,
                                'sync_retry_delay': 5_000,  # ms
                                'sync_retry_nodes': 3,
                                'batch_size': 500_000,  # bytes
                                'max_batch_delay': 100  # ms
                            }
                        }

                        try:
                            for i in range(runs):
                                ret = LocalBench(bench_params, node_params).run(
                                    debug=True).result()

                                log_bench = f'{log_directory}/bench-config{config_id}-f{fault}-n{node}-r{r}-s{size}-{i}.log'
                                print(
                                    f"> Guardando resultados en: {log_bench}")
                                with open(log_bench, 'w') as f:
                                    f.write(ret)
                                print(ret)

                                # Esperar unos segundos para que se liberen los puertos
                                if i != runs - 1:
                                    delay = 8*node/10
                                    print(
                                        f"> Esperando {delay} segundos para arrancar la iteración {i+1}...")
                                    time.sleep(delay)
                        except BenchError as e:
                            Print.error(e)

# Función para cargar los datos de un archivo genérico


def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

# Función para cargar los datos de un archivo CSV


def load_data_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [dict(row) for row in reader]
    print('Data:', data)
    return data

# Función para calcular el promedio y el margen de error


def calculate_statistics(values):
    average = sum(values) / len(values)
    error = 1.96 * (sum((x - average) ** 2 for x in values) /
                    len(values)) ** 0.5
    return average, error

# Función para plotear las gráficas de una configuración y guardarlas como una sola imagen


def save_configuration_plots(config_name, x_values, tps_values, latency_values):
    plt.figure(figsize=(12, 8))

    # Gráfica X vs TPS
    plt.subplot(1, 3, 1)
    plt.errorbar(x_values, tps_values[:, 0], yerr=tps_values[:, 1], marker='o')
    plt.xlabel(config_name)
    plt.ylabel('TPS')
    plt.title(f'{config_name} vs TPS')

    # Gráfica X vs Latency
    plt.subplot(1, 3, 2)
    plt.errorbar(x_values, latency_values[:, 0],
                 yerr=latency_values[:, 1], marker='o')
    plt.xlabel(config_name)
    plt.ylabel('Latency')
    plt.title(f'{config_name} vs Latency')

    # Gráfica TPS vs Latency
    plt.subplot(1, 3, 3)
    plt.scatter(tps_values[:, 0], latency_values[:, 0], marker='o')
    plt.xlabel('TPS')
    plt.ylabel('Latency')
    plt.title('TPS vs Latency')

    plt.tight_layout()  # Ajustar el espaciado entre las gráficas
    plt.savefig(f'{config_name}_plots.png')
    plt.close()


def plot_preprocessing_logs():
    if not os.path.exists(csv_directory):
        os.makedirs(csv_directory)
    for config_id, params in config.items():
        faults = params['faults']
        nodes = params['nodes']
        rate = params['rate']
        tx_size = params['tx_size']
        runs = params['runs']

        data_current_config = []
        data_iterations = []
        data_headers = 'Faults,Nodes,Transaction Rate,Transaction Size,TPS,Latency\n'
        for fault in faults:
            for node in nodes:
                for r in rate:
                    for size in tx_size:
                        for i in range(runs):
                            # Ruta local al archivo de resultados
                            file_path = f'{log_directory}/bench-config{config_id}-f{fault}-n{node}-r{r}-s{size}-{i}.log'

                            # Leer archivo de resultados
                            if not os.path.isfile(file_path):
                                print(f'File does not exist: {file_path}')
                                break

                            data = load_data(file_path)

                            # Extraer métricas de los resultados
                            metrics_data = {}
                            metrics = ['Consensus TPS', 'Consensus latency', 'Faults',
                                       'Committee size', 'Input rate', 'Transaction size']
                            for metric in metrics:
                                pattern = rf'{metric}:\s+([\d,\.]+)'
                                match = re.search(pattern, data)
                                if match:
                                    value = float(
                                        match.group(1).replace(',', ''))
                                    metrics_data[metric] = value
                                else:
                                    metrics_data[metric] = None
                            data_iteration = f'{metrics_data["Faults"]},{metrics_data["Committee size"]},{metrics_data["Input rate"]},{metrics_data["Transaction size"]},{metrics_data["Consensus TPS"]},{metrics_data["Consensus latency"]}'
                            data_iterations.append(data_iteration)

                        # Si no se ejecutó ninguna iteración, no se generará el archivo CSV
                        if len(data_iterations) == 0:
                            continue

                        # Adjuntaremos los resultados al archivo de resumen
                        summary_file = f'{csv_directory}/bench-summary-config{config_id}-f{fault}-n{node}-r{r}-s{size}.csv'
                        with open(summary_file, 'w') as file:
                            file.write(data_headers)
                            for data in data_iterations:
                                file.write(f'{data}\n')
                                data_current_config.append(data)
                        data_iterations = []

        # Si no se ejecutó la configuración, no se generará el archivo CSV
        if len(data_current_config) == 0:
            continue

        # Adjuntaremos los resultados al archivo de resumen
        summary_file = f'{csv_directory}/bench-summary-config{config_id}.csv'
        with open(summary_file, 'w') as file:
            file.write(data_headers)
            for data in data_current_config:
                file.write(f'{data}\n')


@task
def plotting(ctx):
    # Preprocesando los logs generados por el benchmark y guardando los resultados en archivos CSV con un formato específico
    plot_preprocessing_logs()

    # Esperar unos segundos para que carguen los datos
    print('Esperando 5 segundos para cargar los datos...')
    time.sleep(5)

    for i, metric in enumerate(['Faults', 'Nodes', 'Transaction Size']):
        plot_metric(metric, f'{csv_directory}/bench-summary-config{i+1}.csv')
