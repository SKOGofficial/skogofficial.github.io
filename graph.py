import pandas as pd
import altair as alt

# Updated data with recent models and more precise estimates/assumptions
data = {
    'LLM': [
        'GPT-3',
        'GPT-4-like (older est.)', # Clarified this is an older estimate
        'GPT-4o',
        'LLaMA-65B',
        'Llama 3.3 70B FP8',
        'Google Gemini 2.0 Flash',
        'Google Gemini 2.0 Flash Lite'
    ],
    'Computational Capability (Parameters/Context)': [
        '175B parameters',
        'GPT-4-like (general usage)',
        'Latest OpenAI model (high capability)',
        '65B parameters',
        '70B parameters (optimized)',
        'Lightweight, fast (parameters not disclosed)',
        'Very lightweight, efficient (parameters not disclosed)'
    ],
    'Energy Consumption per Token (Original Unit)': [
        '0.004 kWh per ~300 words', # Approximately 300 words = 450 tokens (using 1 word = 1.5 tokens)
        '0.3 Wh per query (assumed 100 tokens)', # Original estimate for GPT-4-like
        '0.3 Wh per query (assumed 500 tokens)', # New estimate for GPT-4o
        '3-4 Joules per output token',
        '0.39 Joules per token',
        '0.022 Wh per query (assumed 900 tokens)',
        '0.016 Wh per query (assumed 900 tokens)'
    ],
    'Source Notes': [
        'Research papers (pre-2023 hardware)',
        'Early third-party estimates for GPT-4-like usage',
        'Recent estimates by Epoch AI, Undetectable AI, Towards Data Science',
        'Samsi et al., 2023',
        'Lin 2025 (H100 node with vLLM, high concurrency)',
        'David Shettler, Medium (estimation based on API pricing)',
        'David Shettler, Medium (estimation based on API pricing)'
    ]
}

df = pd.DataFrame(data)

# Convert all energy units to Joules per token
# Assuming 1 word = 1.5 tokens for conversion
def convert_to_joules_per_token(row):
    original_unit = row['Energy Consumption per Token (Original Unit)']
    if 'kWh' in original_unit:
        value = float(original_unit.split(' ')[0])
        words = float(original_unit.split('~')[1].split(' ')[0])
        tokens = words * 1.5
        return (value * 3.6e6) / tokens # kWh to Joules
    elif 'Joules' in original_unit:
        value_range = original_unit.split(' ')[0].split('-')
        if len(value_range) > 1:
            return (float(value_range[0]) + float(value_range[1])) / 2 # Take average if range
        else:
            return float(value_range[0])
    elif 'Wh' in original_unit:
        value = float(original_unit.split(' ')[0])
        if 'assumed 100 tokens' in original_unit:
            tokens = 100
        elif 'assumed 500 tokens' in original_unit:
            tokens = 500
        elif 'assumed 900 tokens' in original_unit:
            tokens = 900
        else:
            # Fallback or error if assumption not found. This case should not happen with current data.
            return None
        return (value * 3600) / tokens # Wh to Joules

df['Energy Consumption per Token (Joules)'] = df.apply(convert_to_joules_per_token, axis=1)

# Sort the DataFrame by 'Energy Consumption per Token (Joules)'
df_sorted = df.sort_values('Energy Consumption per Token (Joules)', ascending=False)

# Display the table
print("Updated LLM Energy Consumption per Token Table:")
print(df_sorted[['LLM', 'Computational Capability (Parameters/Context)', 'Energy Consumption per Token (Joules)', 'Source Notes']].to_markdown(index=False, numalign="left", stralign="left"))

# Create the bar chart
chart = alt.Chart(df_sorted).mark_bar().encode(
    x=alt.X('LLM', sort='-y', title='LLM'),
    y=alt.Y('Energy Consumption per Token (Joules)', title='Energy Consumption per Token (Joules)'),
    tooltip=[
        'LLM',
        'Computational Capability (Parameters/Context)',
        alt.Tooltip('Energy Consumption per Token (Joules)', format='.3f'),
        'Source Notes'
    ]
).properties(
    title='LLM Energy Consumption per Token (with Recent Models)'
).interactive()

chart.save('llm_energy_consumption_per_token_updated_bar_chart.json')