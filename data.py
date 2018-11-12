import sys
import pandas as pd
import preprocess

# Wipers ==> 1          # Number6 ==> 6     # Finalm ve ==> 11
# Number7 ==> 2         # Salute ==> 7
# Chicken ==> 3         # Mermain ==> 8
# SideStep ==> 4        # Swing ==> 9
# TurnClap ==> 5        # Cowboy ==> 10
def prepare_data(csv_name, number, interval=76, preprocess=True):
    df = pd.read_csv(sys.path[0] + '/data/' + csv_name + '.csv', header=None, preprocess=preprocess)
#    df = preprocess.normalise(df, preprocess=preprocess)
    if preprocess:
        df_max_min = preprocess.flatten(df, interval, preprocess=preprocess)
        df_std = preprocess.flatten(df, 'std', interval, preprocess=preprocess)
        df_concat = preprocess.concat_df(df_max_min, df_std, preprocess=preprocess)
        df = preprocess.append_truth(df_concat, number, preprocess=preprocess)

    return df

def load(with_names=False, preprocess=True):
    all_dfs = []

    sarah_wipers_df = prepare_data('sarah_wipers_2.5min', 1, preprocess=preprocess)
    sarah_number7_df = prepare_data('sarah_number7_2.5min', 2, preprocess=preprocess)
    sarah_chicken_df = prepare_data('sarah_chicken_2.5min', 3, preprocess=preprocess)
    sarah_sidestep_df = prepare_data('sarah_sidestep_2.5min', 4, preprocess=preprocess)
    sarah_turnclap1_df = prepare_data('sarah_turnclap1_1min', 5, preprocess=preprocess)
    sarah_turnclap2_df = prepare_data('sarah_turnclap2_1min', 5, preprocess=preprocess)
    sarah_number6_df = prepare_data('sarah_number6_2.5min', 6, preprocess=preprocess)
    sarah_salute_df = prepare_data('sarah_salute_2.5min', 7, preprocess=preprocess)
    sarah_mermaid_df = prepare_data('sarah_mermaid_2.5min', 8, preprocess=preprocess)
    sarah_swing_df = prepare_data('sarah_swing_2.5min', 9, preprocess=preprocess)
    sarah_cowboy1_df = prepare_data('sarah_cowboy1_1min', 10, preprocess=preprocess)
    sarah_cowboy2_df = prepare_data('sarah_cowboy2_1min', 10, preprocess=preprocess)
    sarah_finalmove_df = prepare_data('sarah_finalmove_2.5min', 11, preprocess=preprocess)

    sarah_wipers_oct_df = prepare_data('sarah_wipers_2.5min_oct', 1, preprocess=preprocess)
    sarah_number7_oct_df = prepare_data('sarah_number7_2.5min_oct', 2, preprocess=preprocess)
    sarah_chicken_oct_df = prepare_data('sarah_chicken_2.5min_oct', 3, preprocess=preprocess)
    sarah_sidestep_oct_df = prepare_data('sarah_sidestep_2.5min_oct', 4, preprocess=preprocess)
    sarah_turnclap1_oct_df = prepare_data('sarah_turnclap1_1min_oct', 5, preprocess=preprocess)
    sarah_turnclap2_oct_df = prepare_data('sarah_turnclap2_1min_oct', 5, preprocess=preprocess)
    sarah_number6_oct_df = prepare_data('sarah_number6_2.5min_oct', 6, preprocess=preprocess)
    sarah_salute_oct_df = prepare_data('sarah_salute_2.5min_oct', 7, preprocess=preprocess)
    sarah_mermaid_oct_df = prepare_data('sarah_mermaid_2.5min_oct', 8, preprocess=preprocess)
    sarah_swing_oct_df = prepare_data('sarah_swing_2.5min_oct', 9, preprocess=preprocess)
    sarah_cowboy1_oct_df = prepare_data('sarah_cowboy1_1min_oct', 10, preprocess=preprocess)
    sarah_cowboy2_oct_df = prepare_data('sarah_cowboy2_1min_oct', 10, preprocess=preprocess)

    stanley_wipers_df = prepare_data('stanley_wipers_2.5min', 1, preprocess=preprocess)
    stanley_number7_df = prepare_data('stanley_number7_2.5min', 2, preprocess=preprocess)
    stanley_chicken_df = prepare_data('stanley_chicken_2.5min', 3, preprocess=preprocess)
    stanley_sidestep_df = prepare_data('stanley_sidestep_2.5min', 4, preprocess=preprocess)
    stanley_turnclap1_df = prepare_data('stanley_turnclap1_1min', 5, preprocess=preprocess)
    stanley_turnclap2_df = prepare_data('stanley_turnclap2_1min', 5, preprocess=preprocess)
    stanley_number6_df = prepare_data('stanley_number6_2.5min', 6, preprocess=preprocess)
    stanley_salute_df = prepare_data('stanley_salute_2.5min', 7, preprocess=preprocess)
    stanley_mermaid_df = prepare_data('stanley_mermaid_2.5min', 8, preprocess=preprocess)
    stanley_swing_df = prepare_data('stanley_swing_2.5min', 9, preprocess=preprocess)
    stanley_cowboy1_df = prepare_data('stanley_cowboy1_1min', 10, preprocess=preprocess)
    stanley_cowboy2_df = prepare_data('stanley_cowboy2_1min', 10, preprocess=preprocess)
    stanley_finalmove_df = prepare_data('stanley_finalmove_2.5min', 11, preprocess=preprocess)

    stanley_wipers_oct_df = prepare_data('stanley_wipers_2.5min_oct', 1, preprocess=preprocess)
    stanley_number7_oct_df = prepare_data('stanley_number7_2.5min_oct', 2, preprocess=preprocess)
    stanley_chicken_oct_df = prepare_data('stanley_chicken_2.5min_oct', 3, preprocess=preprocess)
    stanley_sidestep_oct_df = prepare_data('stanley_sidestep_2.5min_oct', 4, preprocess=preprocess)
    stanley_turnclap1_oct_df = prepare_data('stanley_turnclap1_1min_oct', 5, preprocess=preprocess)
    stanley_turnclap2_oct_df = prepare_data('stanley_turnclap2_1min_oct', 5, preprocess=preprocess)
    stanley_number6_oct_df = prepare_data('stanley_number6_2.5min_oct', 6, preprocess=preprocess)
    stanley_salute_oct_df = prepare_data('stanley_salute_2.5min_oct', 7, preprocess=preprocess)
    stanley_mermaid_oct_df = prepare_data('stanley_mermaid_2.5min_oct', 8, preprocess=preprocess)
    stanley_swing_oct_df = prepare_data('stanley_swing_2.5min_oct', 9, preprocess=preprocess)
    stanley_cowboy1_oct_df = prepare_data('stanley_cowboy1_1min_oct', 10, preprocess=preprocess)
    stanley_cowboy2_oct_df = prepare_data('stanley_cowboy2_1min_oct', 10, preprocess=preprocess)

    azizi_wipers_df = prepare_data('azizi_wipers_2.5min', 1, preprocess=preprocess)
    azizi_number7_df = prepare_data('azizi_number7_2.5min', 2, preprocess=preprocess)
    azizi_chicken_df = prepare_data('azizi_chicken_2.5min', 3, preprocess=preprocess)
    azizi_sidestep_df = prepare_data('azizi_sidestep_2.5min', 4, preprocess=preprocess)
    azizi_turnclap1_df = prepare_data('azizi_turnclap1_1min', 5, preprocess=preprocess)
    azizi_turnclap2_df = prepare_data('azizi_turnclap2_1min', 5, preprocess=preprocess)
    azizi_number6_df = prepare_data('azizi_number6_2.5min', 6, preprocess=preprocess)
    azizi_salute_df = prepare_data('azizi_salute_2.5min', 7, preprocess=preprocess)
    azizi_mermaid_df = prepare_data('azizi_mermaid_2.5min', 8, preprocess=preprocess)
    azizi_swing_df = prepare_data('azizi_swing_2.5min', 9, preprocess=preprocess)
    azizi_cowboy1_df = prepare_data('azizi_cowboy1_1min', 10, preprocess=preprocess)
    azizi_cowboy2_df = prepare_data('azizi_cowboy2_1min', 10, preprocess=preprocess)
    azizi_finalmove_df = prepare_data('azizi_finalmove_2.5min', 11, preprocess=preprocess)

    azizi_wipers_oct_df = prepare_data('azizi_wipers_2.5min_oct', 1, preprocess=preprocess)
    azizi_number7_oct_df = prepare_data('azizi_number7_2.5min_oct', 2, preprocess=preprocess)
    azizi_chicken_oct_df = prepare_data('azizi_chicken_2.5min_oct', 3, preprocess=preprocess)
    azizi_sidestep_oct_df = prepare_data('azizi_sidestep_2.5min_oct', 4, preprocess=preprocess)
    azizi_turnclap1_oct_df = prepare_data('azizi_turnclap1_1min_oct', 5, preprocess=preprocess)
    azizi_turnclap2_oct_df = prepare_data('azizi_turnclap2_1min_oct', 5, preprocess=preprocess)
    azizi_number6_oct_df = prepare_data('azizi_number6_2.5min_oct', 6, preprocess=preprocess)
    azizi_salute_oct_df = prepare_data('azizi_salute_2.5min_oct', 7, preprocess=preprocess)
    azizi_mermaid_oct_df = prepare_data('azizi_mermaid_2.5min_oct', 8, preprocess=preprocess)
    azizi_swing_oct_df = prepare_data('azizi_swing_2.5min_oct', 9, preprocess=preprocess)
    azizi_cowboy1_oct_df = prepare_data('azizi_cowboy1_1min_oct', 10, preprocess=preprocess)
    azizi_cowboy2_oct_df = prepare_data('azizi_cowboy2_1min_oct', 10, preprocess=preprocess)

    kaiyan_wipers_df = prepare_data('kaiyan_wipers_2.5min', 1, preprocess=preprocess)
    kaiyan_number7_df = prepare_data('kaiyan_number7_2.5min', 2, preprocess=preprocess)
    kaiyan_chicken_df = prepare_data('kaiyan_chicken_2.5min', 3, preprocess=preprocess)
    kaiyan_sidestep_df = prepare_data('kaiyan_sidestep_2.5min', 4, preprocess=preprocess)
    kaiyan_turnclap1_df = prepare_data('kaiyan_turnclap1_1min', 5, preprocess=preprocess)
    kaiyan_turnclap2_df = prepare_data('kaiyan_turnclap2_1min', 5, preprocess=preprocess)
    kaiyan_number6_df = prepare_data('kaiyan_number6_2.5min', 6, preprocess=preprocess)
    kaiyan_salute_df = prepare_data('kaiyan_salute_2.5min', 7, preprocess=preprocess)
    kaiyan_mermaid_df = prepare_data('kaiyan_mermaid_2.5min', 8, preprocess=preprocess)
    kaiyan_swing_df = prepare_data('kaiyan_swing_2.5min', 9, preprocess=preprocess)
    kaiyan_cowboy1_df = prepare_data('kaiyan_cowboy1_1min', 10, preprocess=preprocess)
    kaiyan_cowboy2_df = prepare_data('kaiyan_cowboy2_1min', 10, preprocess=preprocess)
    kaiyan_finalmove_df = prepare_data('kaiyan_finalmove_2.5min', 11, preprocess=preprocess)

    calvin_wipers_df = prepare_data('calvin_wipers_2.5min', 1, preprocess=preprocess)
    calvin_number7_df = prepare_data('calvin_number7_2.5min', 2, preprocess=preprocess)
    calvin_chicken_df = prepare_data('calvin_chicken_2.5min', 3, preprocess=preprocess)
    calvin_sidestep_df = prepare_data('calvin_sidestep_2.5min', 4, preprocess=preprocess)
    calvin_turnclap1_df = prepare_data('calvin_turnclap1_1min', 5, preprocess=preprocess)
    calvin_turnclap2_df = prepare_data('calvin_turnclap2_1min', 5, preprocess=preprocess)
    calvin_number6_df = prepare_data('calvin_number6_2.5min', 6, preprocess=preprocess)
    calvin_salute_df = prepare_data('calvin_salute_2.5min', 7, preprocess=preprocess)
    calvin_mermaid_df = prepare_data('calvin_mermaid_2.5min', 8, preprocess=preprocess)
    calvin_swing_df = prepare_data('calvin_swing_2.5min', 9, preprocess=preprocess)
    calvin_cowboy1_df = prepare_data('calvin_cowboy1_1min', 10, preprocess=preprocess)
    calvin_cowboy2_df = prepare_data('calvin_cowboy2_1min', 10, preprocess=preprocess)
    calvin_finalmove_df = prepare_data('calvin_finalmove_2.5min', 11, preprocess=preprocess)

    calvin_wipers_oct_df = prepare_data('calvin_wipers_3min_oct', 1, preprocess=preprocess)
    calvin_number7_oct_df = prepare_data('calvin_number7_3min_oct', 2, preprocess=preprocess)
    calvin_chicken_oct_df = prepare_data('calvin_chicken_3min_oct', 3, preprocess=preprocess)
    calvin_sidestep_oct_df = prepare_data('calvin_sidestep_3min_oct', 4, preprocess=preprocess)
    calvin_turnclap1_oct_df = prepare_data('calvin_turnclap1_1min_oct', 5, preprocess=preprocess)
    calvin_turnclap2_oct_df = prepare_data('calvin_turnclap2_1min_oct', 5, preprocess=preprocess)
    calvin_number6_oct_df = prepare_data('calvin_number6_3min_oct', 6, preprocess=preprocess)
    calvin_salute_oct_df = prepare_data('calvin_salute_2.5min_oct', 7, preprocess=preprocess)
    calvin_mermaid_oct_df = prepare_data('calvin_mermaid_3min_oct', 8, preprocess=preprocess)
    calvin_swing_oct_df = prepare_data('calvin_swing_3min_oct', 9, preprocess=preprocess)
    calvin_cowboy1_oct_df = prepare_data('calvin_cowboy1_1min_oct', 10, preprocess=preprocess)
    calvin_cowboy2_oct_df = prepare_data('calvin_cowboy2_1min_oct', 10, preprocess=preprocess)

    gary_wipers_oct_df = prepare_data('gary_wipers_3min_oct', 1, preprocess=preprocess)
    gary_number7_oct_df = prepare_data('gary_number7_3min_oct', 2, preprocess=preprocess)
    gary_chicken_oct_df = prepare_data('gary_chicken_3min_oct', 3, preprocess=preprocess)
    gary_sidestep_oct_df = prepare_data('gary_sidestep_3min_oct', 4, preprocess=preprocess)
    gary_turnclap1_oct_df = prepare_data('gary_turnclap1_1min_oct', 5, preprocess=preprocess)
    gary_turnclap2_oct_df = prepare_data('gary_turnclap2_1min_oct', 5, preprocess=preprocess)
    gary_number6_oct_df = prepare_data('gary_number6_2.5min_oct', 6, preprocess=preprocess)
    gary_salute_oct_df = prepare_data('gary_salute_3min_oct', 7, preprocess=preprocess)
    gary_mermaid_oct_df = prepare_data('gary_mermaid_3min_oct', 8, preprocess=preprocess)
    gary_swing_oct_df = prepare_data('gary_swing_3min_oct', 9, preprocess=preprocess)
    gary_cowboy1_oct_df = prepare_data('gary_cowboy1_1min_oct', 10, preprocess=preprocess)
    gary_cowboy2_oct_df = prepare_data('gary_cowboy2_1min_oct', 10, preprocess=preprocess)

    gary_wipers_df = prepare_data('gary_wipers_2.5min', 1, preprocess=preprocess)
    gary_number7_df = prepare_data('gary_number7_2.5min', 2, preprocess=preprocess)
    gary_chicken_df = prepare_data('gary_chicken_2.5min', 3, preprocess=preprocess)
    gary_sidestep_df = prepare_data('gary_sidestep_2.5min', 4, preprocess=preprocess)
    gary_turnclap1_df = prepare_data('gary_turnclap1_1min', 5, preprocess=preprocess)
    gary_turnclap2_df = prepare_data('gary_turnclap2_1min', 5, preprocess=preprocess)
    gary_number6_df = prepare_data('gary_number6_2.5min', 6, preprocess=preprocess)
    gary_salute_df = prepare_data('gary_salute_2.5min', 7, preprocess=preprocess)
    gary_mermaid_df = prepare_data('gary_mermaid_2.5min', 8, preprocess=preprocess)
    gary_swing_df = prepare_data('gary_swing_2.5min', 9, preprocess=preprocess)
    gary_cowboy1_df = prepare_data('gary_cowboy1_1min', 10, preprocess=preprocess)
    gary_cowboy2_df = prepare_data('gary_cowboy2_1min', 10, preprocess=preprocess)
    gary_finalmove_df = prepare_data('gary_finalmove_2.5min', 11, preprocess=preprocess)

    all_dfs.extend([
        sarah_wipers_df,sarah_number7_df,sarah_chicken_df,sarah_sidestep_df,
        sarah_turnclap1_df,sarah_turnclap2_df,sarah_number6_df,sarah_salute_df,sarah_mermaid_df,sarah_swing_df,
        sarah_cowboy1_df,sarah_cowboy2_df,sarah_finalmove_df,
        sarah_wipers_oct_df,sarah_number7_oct_df,sarah_chicken_oct_df,sarah_sidestep_oct_df,
        sarah_turnclap1_oct_df,sarah_turnclap2_oct_df,sarah_number6_oct_df,sarah_salute_oct_df,sarah_mermaid_oct_df,sarah_swing_oct_df,
        sarah_cowboy1_oct_df,sarah_cowboy2_oct_df,
        azizi_wipers_df,azizi_number7_df,azizi_chicken_df,azizi_sidestep_df,azizi_salute_df,
        azizi_turnclap1_df,azizi_turnclap2_df,azizi_number6_df,azizi_mermaid_df,azizi_swing_df,
        azizi_cowboy1_df,azizi_cowboy2_df,azizi_finalmove_df,
        azizi_wipers_oct_df,azizi_number7_oct_df,azizi_chicken_oct_df,azizi_sidestep_oct_df,azizi_salute_oct_df,
        azizi_turnclap1_oct_df,azizi_turnclap2_oct_df,azizi_number6_oct_df,azizi_mermaid_oct_df,azizi_swing_oct_df,
        azizi_cowboy1_oct_df,azizi_cowboy2_oct_df,
        stanley_wipers_oct_df,stanley_number7_oct_df,stanley_chicken_oct_df,stanley_sidestep_oct_df,
        stanley_turnclap1_oct_df,stanley_turnclap2_oct_df,stanley_number6_oct_df,stanley_salute_oct_df,stanley_mermaid_oct_df,stanley_swing_oct_df,
        stanley_cowboy1_oct_df,stanley_cowboy2_oct_df,
        stanley_wipers_df,stanley_number7_df,stanley_chicken_df,stanley_sidestep_df,
        stanley_turnclap1_df,stanley_turnclap2_df,stanley_number6_df,stanley_salute_df,stanley_mermaid_df,stanley_swing_df,
        stanley_cowboy1_df,stanley_cowboy2_df,stanley_finalmove_df,
        kaiyan_wipers_df,kaiyan_number7_df,kaiyan_chicken_df,kaiyan_sidestep_df,
        kaiyan_turnclap1_df,kaiyan_turnclap2_df,kaiyan_number6_df,kaiyan_salute_df,kaiyan_mermaid_df,kaiyan_swing_df,
        kaiyan_cowboy1_df,kaiyan_cowboy2_df,kaiyan_finalmove_df,
        calvin_wipers_df,calvin_number7_df,calvin_chicken_df,calvin_sidestep_df,
        calvin_turnclap1_df,calvin_turnclap2_df,calvin_number6_df,calvin_salute_df,calvin_mermaid_df,calvin_swing_df,
        calvin_cowboy1_df,calvin_cowboy2_df,calvin_finalmove_df,
        calvin_wipers_oct_df,calvin_number7_oct_df,calvin_chicken_oct_df,calvin_sidestep_oct_df,
        calvin_turnclap1_oct_df,calvin_turnclap2_oct_df,calvin_number6_oct_df,calvin_salute_oct_df,calvin_mermaid_oct_df,calvin_swing_oct_df,
        calvin_cowboy1_oct_df,calvin_cowboy2_oct_df,
        gary_wipers_df,gary_number7_df,gary_chicken_df,gary_sidestep_df,
        gary_turnclap1_df,gary_turnclap2_df,gary_number6_df,gary_salute_df,gary_mermaid_df,gary_swing_df,
        gary_cowboy1_df,gary_cowboy2_df,gary_finalmove_df,
        gary_wipers_oct_df,gary_number7_oct_df,gary_chicken_oct_df,gary_sidestep_oct_df,
        gary_turnclap1_oct_df,gary_turnclap2_oct_df,gary_number6_oct_df,gary_salute_oct_df,gary_mermaid_oct_df,gary_swing_oct_df,
        gary_cowboy1_oct_df,gary_cowboy2_oct_df
    ])

    if with_names:
        all_names = []
        all_names.extend([
            'sarah_wipers_df' ,'sarah_number7_df' ,'sarah_chicken_df' ,'sarah_sidestep_df',
            'sarah_turnclap1_df' ,'sarah_turnclap2_df' ,'sarah_number6_df' ,'sarah_salute_df' ,'sarah_mermaid_df' ,'sarah_swing_df',
            'sarah_cowboy1_df' ,'sarah_cowboy2_df' ,'sarah_finalmove_df',
            'sarah_wipers_oct_df' ,'sarah_number7_oct_df' ,'sarah_chicken_oct_df' ,'sarah_sidestep_oct_df',
            'sarah_turnclap1_oct_df' ,'sarah_turnclap2_oct_df' ,'sarah_number6_oct_df' ,'sarah_salute_oct_df' ,'sarah_mermaid_oct_df' ,'sarah_swing_oct_df',
            'sarah_cowboy1_oct_df' ,'sarah_cowboy2_oct_df',
            'azizi_wipers_df' ,'azizi_number7_df' ,'azizi_chicken_df' ,'azizi_sidestep_df' ,'azizi_salute_df',
            'azizi_turnclap1_df' ,'azizi_turnclap2_df' ,'azizi_number6_df' ,'azizi_mermaid_df' ,'azizi_swing_df',
            'azizi_cowboy1_df' ,'azizi_cowboy2_df' ,'azizi_finalmove_df',
            'azizi_wipers_oct_df' ,'azizi_number7_oct_df' ,'azizi_chicken_oct_df' ,'azizi_sidestep_oct_df' ,'azizi_salute_oct_df',
            'azizi_turnclap1_oct_df' ,'azizi_turnclap2_oct_df' ,'azizi_number6_oct_df' ,'azizi_mermaid_oct_df' ,'azizi_swing_oct_df',
            'azizi_cowboy1_oct_df' ,'azizi_cowboy2_oct_df',
            'stanley_wipers_oct_df' ,'stanley_number7_oct_df' ,'stanley_chicken_oct_df' ,'stanley_sidestep_oct_df',
            'stanley_turnclap1_oct_df' ,'stanley_turnclap2_oct_df' ,'stanley_number6_oct_df' ,'stanley_salute_oct_df' ,'stanley_mermaid_oct_df' ,'stanley_swing_oct_df',
            'stanley_cowboy1_oct_df' ,'stanley_cowboy2_oct_df',
            'stanley_wipers_df' ,'stanley_number7_df' ,'stanley_chicken_df' ,'stanley_sidestep_df',
            'stanley_turnclap1_df' ,'stanley_turnclap2_df' ,'stanley_number6_df' ,'stanley_salute_df' ,'stanley_mermaid_df' ,'stanley_swing_df',
            'stanley_cowboy1_df' ,'stanley_cowboy2_df' ,'stanley_finalmove_df',
            'kaiyan_wipers_df' ,'kaiyan_number7_df' ,'kaiyan_chicken_df' ,'kaiyan_sidestep_df',
            'kaiyan_turnclap1_df' ,'kaiyan_turnclap2_df' ,'kaiyan_number6_df' ,'kaiyan_salute_df' ,'kaiyan_mermaid_df' ,'kaiyan_swing_df',
            'kaiyan_cowboy1_df' ,'kaiyan_cowboy2_df' ,'kaiyan_finalmove_df',
            'calvin_wipers_df' ,'calvin_number7_df' ,'calvin_chicken_df' ,'calvin_sidestep_df',
            'calvin_turnclap1_df' ,'calvin_turnclap2_df' ,'calvin_number6_df' ,'calvin_salute_df' ,'calvin_mermaid_df' ,'calvin_swing_df',
            'calvin_cowboy1_df' ,'calvin_cowboy2_df' ,'calvin_finalmove_df',
            'calvin_wipers_oct_df' ,'calvin_number7_oct_df' ,'calvin_chicken_oct_df' ,'calvin_sidestep_oct_df',
            'calvin_turnclap1_oct_df' ,'calvin_turnclap2_oct_df' ,'calvin_number6_oct_df' ,'calvin_salute_oct_df' ,'calvin_mermaid_oct_df' ,'calvin_swing_oct_df',
            'calvin_cowboy1_oct_df' ,'calvin_cowboy2_oct_df',
            'gary_wipers_df' ,'gary_number7_df' ,'gary_chicken_df' ,'gary_sidestep_df',
            'gary_turnclap1_df' ,'gary_turnclap2_df' ,'gary_number6_df' ,'gary_salute_df' ,'gary_mermaid_df' ,'gary_swing_df',
            'gary_cowboy1_df' ,'gary_cowboy2_df' ,'gary_finalmove_df',
            'gary_wipers_oct_df' ,'gary_number7_oct_df' ,'gary_chicken_oct_df' ,'gary_sidestep_oct_df',
            'gary_turnclap1_oct_df' ,'gary_turnclap2_oct_df' ,'gary_number6_oct_df' ,'gary_salute_oct_df' ,'gary_mermaid_oct_df' ,'gary_swing_oct_df',
            'gary_cowboy1_oct_df' ,'gary_cowboy2_oct_df'
        ])

        return (all_dfs, all_names)

    return all_dfs
