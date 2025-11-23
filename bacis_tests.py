from stress_assessment import calculate_stress_score, get_stress_level
from config import SCORING_RANGES

def test_stress_assessment():
    """Basic tests for the stress assessment module"""
    print("Running basic tests...")
    
    # Test scoring calculation
    test_answers = [2, 3, 2, 4, 3]  # Should total 14
    score = calculate_stress_score(test_answers)
    level = get_stress_level(score)
    
    print(f"Test Score: {score} -> Level: {level}")
    
    # Verify results
    assert score == 14, f"Expected 14, got {score}"
    assert level == "Moderate Stress", f"Expected 'Moderate Stress', got '{level}'"
    
    print("✅ All basic tests passed!")
    print("✅ Stress assessment module is working correctly")

if __name__ == "__main__":
    test_stress_assessment()