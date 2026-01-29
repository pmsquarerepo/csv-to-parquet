from src.clean import clean_csv

def test_clean_csv(tmp_path):
    p = tmp_path / "test.csv"
    p.write_text("a,b\n1,2\n1,2\n")
    df = clean_csv(p)
    assert len(df) == 1
