import os

def generate_sh_script(directory, output_file):
    # List all files in the specified directory
    files = os.listdir(directory)
    
    # Filter out only YAML files
    yaml_files = [f for f in files if f.endswith('.yaml')]
    
    # Open the output file for writing
    with open(output_file, 'w') as f:
        for yaml_file in yaml_files:
            # Generate the command for each YAML file
            command = f"CUDA_VISIBLE_DEVICES=2 python MotionDirector_train.py --config {os.path.join(directory, yaml_file)}"
            # Write the command to the output file
            f.write(command + '\n')

# Specify the directory containing the YAML files and the output sh file name
directory = 'ucf/ucf_yaml'
output_file = 'train.sh'

# Generate the sh script
generate_sh_script(directory, output_file)

print(f'Script {output_file} generated successfully.')
