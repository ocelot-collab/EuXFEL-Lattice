import euxfel.sequences as sequences


def test_get_sequences():
    # Just check they exist in some form and subsequence modules are in some sense "normal".
    sequences.cathode_to_i1d
    sequences.cathode_to_b1d
    sequences.cathode_to_b2d
    sequences.cathode_to_tld
    sequences.cathode_to_t4d
    sequences.cathode_to_t5d
