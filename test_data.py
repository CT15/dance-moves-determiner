import sys
import pandas as pd
import preprocess as prep

# Wipers ==> 1          # Number6 ==> 6     # Finalm ve ==> 11
# Number7 ==> 2         # Salute ==> 7
# Chicken ==> 3         # Mermain ==> 8
# SideStep ==> 4        # Swing ==> 9
# TurnClap ==> 5        # Cowboy ==> 10
def prepare_data(csv_name, number, interval=76):
    df = pd.read_csv(sys.path[0] + '/train_data/' + csv_name + '.csv', header=None)
#    df = preprocess.normalise(df)
    df_max_min = prep.flatten(df, interval)
    df_var = prep.flatten(df, 'var', interval)
    df_concat = prep.concat_df(df_max_min, df_var)
    df = prep.append_truth(df_concat, number)

    return df


def load(with_names=False):
    all_tests = []

    sarah_wipers_test = prepare_data('sarah_wipers_test', 1)
    sarah_number7_test = prepare_data('sarah_number7_test', 2)
    sarah_chicken_test = prepare_data('sarah_chicken_test', 3)
    sarah_sidestep_test = prepare_data('sarah_sidestep_test', 4)
    sarah_turnclap1_test = prepare_data('sarah_turnclap1_1min', 5)
    sarah_turnclap2_test = prepare_data('sarah_turnclap2_1min', 5)
    sarah_number6_test = prepare_data('sarah_number6_test', 6)
    sarah_salute_test = prepare_data('sarah_salute_test', 7)
    sarah_mermaid_test = prepare_data('sarah_mermaid_test', 8)
    sarah_swing_test = prepare_data('sarah_swing_test', 9)
    sarah_cowboy1_test = prepare_data('sarah_cowboy1_1min', 10)
    sarah_cowboy2_test = prepare_data('sarah_cowboy2_1min', 10)
    sarah_finalmove_test = prepare_data('sarah_finalmove_test', 11)
    
    all_tests.extend([
        sarah_wipers_test, sarah_number7_test, sarah_chicken_test, sarah_sidestep_test,
        sarah_turnclap1_test, sarah_turnclap2_test, sarah_number6_test, sarah_salute_test,
        sarah_mermaid_test, sarah_swing_test, sarah_cowboy1_test, sarah_cowboy2_test,
        sarah_finalmove_test
    ])

    if with_names:
        all_names = []
        all_names.extend([
            'sarah_wipers_test', 'sarah_number7_test', 'sarah_chicken_test', 'sarah_sidestep_test',
            'sarah_turnclap1_test', 'sarah_turnclap2_test', 'sarah_number6_test', 'sarah_salute_test',
            'sarah_mermaid_test', 'sarah_swing_test', 'sarah_cowboy1_test', 'sarah_cowboy2_test',
            'sarah_finalmove_test'
        ])
        return (all_tests, all_names)

    return all_tests
