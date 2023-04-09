import pandas as pd
import sys
import os
import matplotlib.pyplot as plt



# Get the current working directory
cwd = os.getcwd()

# Create a list of all the xlsx files in the directory
xlsx_files = [file for file in os.listdir(cwd + '/excels_each_year') if file.endswith('.xlsx')]
sum_each_year={}
# Loop through each xlsx file
for file in xlsx_files:
    # Read the file into a pandas dataframe
    df = pd.read_excel(cwd + '/excels_each_year/' + file)
    
    # Filter the dataframe by the specified criteria
    df = df[(df['单位级别'] == '省级') | (df['单位级别'] == '市级')]
    df = df[df['专业要求'].str.contains('电子|不限')] # Modify the filter to include '电子' or '不限' in the '专业要求' column', '不限'])]

    # Get the year from the filename

    year = file.split('.')[0]

    # Create the output filename
    output_file = year + '_output.xlsx'


    # Write the filtered dataframe to the output file
    df.to_excel(output_file, index=False)

    # Calculate the total recruitment for the year
    sum_recruit = df['招录人数'].sum()

    # Print the total recruitment for the year
    print(f"{year} Total recruit: {sum_recruit}")
    
    # Group the data by year and sum the recruitment numbers for each year
    df_sum = df['招录人数'].sum()  # Sum the recruitment numbers for the filtered dataframe
    sum_each_year[year]=df_sum

    
# Plot the recruitment numbers as a line chart
my_list = sorted(sum_each_year.items())
x,y=zip(*my_list)

plt.plot(x, y, label=year)

# Add a legend to the plot
plt.legend()

# Add axis labels and a title to the plot
plt.title('Recruitment Numbers Each Year')
plt.xlabel('Year')
plt.ylabel('Recruitment Numbers')

# Show the plot
plt.show()

plt.savefig('历年选调招录人数.png', dpi=300, bbox_inches='tight')


# Create a new directory called 'outputs' if it doesn't already exist
if not os.path.exists(cwd + '/outputs'):
    os.mkdir(cwd + '/outputs')

# Move all files ending with 'output.xlsx' to the 'outputs' directory
for file in os.listdir(cwd):
    if file.endswith('output.xlsx'):
        #python中的rename可以移动文件
        os.rename(cwd + '/' + file, cwd + '/outputs/' + file)
