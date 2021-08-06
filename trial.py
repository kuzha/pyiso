from pyiso import client_factory
import pandas as pd

isone = client_factory('IESO')
#isone = client_factory('IESO', timeout_seconds=60)

data = isone.get_generation(latest=True)
df = pd.DataFrame(data)
print(df)