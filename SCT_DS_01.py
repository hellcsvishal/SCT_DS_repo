import wbgapi as wb
import pandas as pd
import matplotlib.pyplot as plt

def fetch_population_data():
    data_series = wb.data.Series('SP.POP.TOTL', mrv=1, simplify_index=True)
        df = data_series.rename('population').to_frame()
            df = df.join(wb.economy.DataFrame()[['name']], how='left')
                df = df.reset_index().rename(columns={'index': 'iso3'})
                    df.dropna(subset=['population'], inplace=True)
                        df['population_millions'] = df['population'] / 1e6
                            return df

                            def plot_population_distribution(df):
                                plt.style.use('seaborn-whitegrid')
                                    plt.figure(figsize=(14, 8))

                                        plt.hist(df['population_millions'], bins=30, color='#4C72B0', edgecolor='black', alpha=0.85)

                                            mean_pop = df['population_millions'].mean()
                                                median_pop = df['population_millions'].median()

                                                    plt.axvline(mean_pop, color='red', linestyle='dashed', linewidth=1.5, label=f'Mean: {mean_pop:.1f}M')
                                                        plt.axvline(median_pop, color='green', linestyle='dotted', linewidth=1.5, label=f'Median: {median_pop:.1f}M')

                                                            plt.title('Distribution of Total Population by Country', fontsize=18)
                                                                plt.xlabel('Population (millions)', fontsize=14)
                                                                    plt.ylabel('Number of Countries', fontsize=14)
                                                                        plt.legend()
                                                                            plt.tight_layout()
                                                                                plt.show()

                                                                                def main():
                                                                                    population_df = fetch_population_data()
                                                                                        if not population_df.empty:
                                                                                                plot_population_distribution(population_df)

                                                                                                if __name__ == "__main__":
                                                                                                    main()
                                                                                                    