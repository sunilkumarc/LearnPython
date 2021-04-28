'''
Write a python function which takes an input filename and output filename
as parameters. This function copies the data from input file to output file.
'''

'''
f = open('new_file.txt', 'w')
f.write('Third line')
f.close()
'''

def copy_data(input_file_name, output_file_name):
    f_in = open(input_file_name, 'r')
    content = f_in.read()
    f_in.close()
    
    # write some code to create output.txt and insert content
    f_out = open(output_file_name, 'w')
    f_out.write(content)
    f_out.close()
    print("Output file created successfully.")

# We need to call the function here
copy_data('input.txt', 'output.txt')