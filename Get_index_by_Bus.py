
# This code returns the index of the Bus name provided, which is used by other program to find the corrosponding fault level in the CSV file
import pandas as pd


def get_index(bus_name):
    df= pd.read_csv('ieee34-2_EXP_FAULTS.CSV')
    df.to_string()
    i = 0
    print(df['Bus'])
    for x in df['Bus']:
        
        if(x.strip() == bus_name):
            return i
        i=i+1
    return(-1)
    pass

if __name__ == '__main__':
    print(get_index("SOURCEBUS"))