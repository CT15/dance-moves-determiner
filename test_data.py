import sys
import pandas as pd
import preprocess as prep

# Wipers ==> 0          # Number6 ==> 5     # Finalm ve ==> 10
# Number7 ==> 1         # Salute ==> 6
# Chicken ==> 2         # Mermain ==> 7
# SideStep ==> 3        # Swing ==> 8
# TurnClap ==> 4        # Cowboy ==> 9
def prepare_data(csv_name, number, interval=60):
    df = pd.read_csv(sys.path[0] + '/test_data/' + csv_name + '.csv', header=None)
#    df = preprocess.normalise(df)
    df_max_min = prep.flatten(df, interval)
    df_var = prep.flatten(df, 'var', interval)
    df_concat = prep.concat_df(df_max_min, df_var)
    df = prep.append_truth(df_concat, number)

    return df


def load(with_names=False):
    all_tests = []

    sarah_wipers_test = prepare_data('sarah_wipers_test', 0)
    sarah_number7_test = prepare_data('sarah_number7_test', 1)
    sarah_chicken_test = prepare_data('sarah_chicken_test', 2)
    sarah_sidestep_test = prepare_data('sarah_sidestep_test', 3)
    sarah_turnclap_test = prepare_data('sarah_turnclap_test', 4)
    sarah_number6_test = prepare_data('sarah_number6_test', 5)
    sarah_salute_test = prepare_data('sarah_salute_test', 6)
    sarah_mermaid_test = prepare_data('sarah_mermaid_test', 7)
    sarah_swing_test = prepare_data('sarah_swing_test', 8)
    sarah_cowboy_test = prepare_data('sarah_cowboy_test', 9)
    sarah_finalmove_test = prepare_data('sarah_finalmove_test', 10)

    all_tests.extend([
        sarah_wipers_test, sarah_number7_test, sarah_chicken_test, sarah_sidestep_test,
        sarah_turnclap_test, sarah_number6_test, sarah_salute_test,
        sarah_mermaid_test, sarah_swing_test, sarah_cowboy_test,
        sarah_finalmove_test
    ])

    if with_names:
        all_names = []
        all_names.extend([
            'sarah_wipers_test', 'sarah_number7_test', 'sarah_chicken_test', 'sarah_sidestep_test',
            'sarah_turnclap_test', 'sarah_number6_test', 'sarah_salute_test',
            'sarah_mermaid_test', 'sarah_swing_test', 'sarah_cowboy_test',
            'sarah_finalmove_test'
        ])
        return (all_tests, all_names)

    return all_tests
