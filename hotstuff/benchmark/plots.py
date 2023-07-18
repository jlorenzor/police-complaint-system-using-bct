import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_metric(metric_selected, filepath):
    # Guardaremos en un plot_directory los plots
    plot_directory = './results/plots'
    if not os.path.exists(plot_directory):
        os.makedirs(plot_directory)

    # Leer los datos del archivo CSV y si no existe, mostrar un error
    if not os.path.isfile(filepath):
        print(f'File does not exist: {filepath}')
        return
    df = pd.read_csv(filepath)

    # Agrupar los datos por la columna de la métrica seleccionada y calcular la media y el error estándar
    grouped_df = df.groupby(metric_selected).agg(
        {'TPS': ['mean', 'sem'], 'Latency': ['mean', 'sem']}).reset_index()
    grouped_df.columns = [metric_selected, 'TPS_mean',
                          'TPS_sem', 'Latency_mean', 'Latency_sem']

    # Crear una figura con un solo subplot
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))

    # Generar la primera gráfica: "Métrica Seleccionada" vs TPS
    axs[0].errorbar(grouped_df[metric_selected].values, grouped_df['TPS_mean'].values,
                    yerr=grouped_df['TPS_sem'].values, fmt='o-', capsize=5)
    axs[0].set_title(f'{metric_selected} vs TPS')
    axs[0].set_xlabel(metric_selected)
    axs[0].set_ylabel('TPS')
    axs[0].xaxis.set_major_locator(plt.MaxNLocator(integer=True))

    # Generar la segunda gráfica: "Métrica Seleccionada" vs Latency
    axs[1].errorbar(grouped_df[metric_selected].values, grouped_df['Latency_mean'].values,
                    yerr=grouped_df['Latency_sem'].values, fmt='o-', capsize=5)
    axs[1].set_title(f'{metric_selected} vs Latency')
    axs[1].set_xlabel(metric_selected)
    axs[1].set_ylabel('Latency')
    axs[1].xaxis.set_major_locator(plt.MaxNLocator(integer=True))

    # Generar la tercera gráfica: TPS vs Latency
    scatter = axs[2].scatter(grouped_df['TPS_mean'].values, grouped_df['Latency_mean'].values,
                             c=grouped_df[metric_selected].values, cmap='viridis', alpha=0.6)
    axs[2].errorbar(grouped_df['TPS_mean'].values, grouped_df['Latency_mean'].values, xerr=grouped_df['TPS_sem'].values,
                    yerr=grouped_df['Latency_sem'].values, fmt='o', capsize=5, color='gray', alpha=0.5)
    axs[2].plot(grouped_df['TPS_mean'].values, grouped_df['Latency_mean'].values,
                linestyle='-', color='gray', alpha=0.5)
    axs[2].set_title('TPS vs Latency')
    axs[2].set_xlabel('TPS')
    axs[2].set_ylabel('Latency')

    # Crear labels personalizados para la leyenda
    labels = [
        f"{metric_selected}: {medition}" for medition in grouped_df[metric_selected].unique()]
    handles = [plt.Line2D([0], [0], marker='o', color='w',
                          markerfacecolor=scatter.cmap(scatter.norm(rate)), markersize=10) for rate in grouped_df[metric_selected].unique()]
    # Agregar una leyenda con la cantidad de la métrica seleccionada
    legend1 = axs[2].legend(
        handles, labels, title=f"{metric_selected}", loc="upper left", bbox_to_anchor=(1, 1))
    axs[2].add_artist(legend1)

    # Ajustar el espaciado entre las gráficas
    plt.subplots_adjust(hspace=0.5)

    # Guardar la figura en un archivo PNG
    plt.savefig(f'{plot_directory}/{metric_selected}.png', bbox_inches='tight')
