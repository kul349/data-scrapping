try:
    import pandas as pd
    import numpy as np
    
    print("pandas version:", pd.__version__)
    print("numpy version:", np.__version__)
    
    # Simple test for pandas
    data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
    df = pd.DataFrame(data)
    print("\nSample DataFrame:\n", df)
    
    # Simple test for numpy
    arr = np.array([1, 2, 3, 4])
    print("\nSample NumPy Array:", arr)

except ImportError as e:
    print("ImportError:", e)

except Exception as e:
    print("An error occurred:", e)
