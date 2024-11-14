import os
import subprocess
from pathlib import Path

def convert_eps_to_png(input_path, output_path=None, dpi=300):
    """
    Convert an EPS file to PNG using Ghostscript.
    
    Args:
        input_path (str): Path to input EPS file
        output_path (str, optional): Path for output PNG file. If None, uses same name as input
        dpi (int, optional): Resolution for output PNG. Defaults to 300
    
    Returns:
        bool: True if conversion successful, False otherwise
    """
    input_path = Path(input_path)
    
    # If no output path specified, use same name as input but with .png extension
    if output_path is None:
        output_path = input_path.with_suffix('.png')
    output_path = Path(output_path)
    
    # Ensure input file exists
    if not input_path.exists():
        print(f"Error: Input file {input_path} does not exist")
        return False
    
    try:
        # Ghostscript command for conversion
        gs_command = [
            'gs',  # ghostscript command
            '-dSAFER',
            '-dBATCH',
            '-dNOPAUSE',
            '-dEPSCrop',
            f'-r{dpi}',
            '-sDEVICE=png16m',
            f'-sOutputFile={output_path}',
            input_path
        ]
        
        # Run the conversion
        subprocess.run(gs_command, check=True, capture_output=True)
        print(f"Successfully converted {input_path} to {output_path}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_path}: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error converting {input_path}: {e}")
        return False

def batch_convert_directory(input_dir, output_dir=None, dpi=300):
    """
    Convert all EPS files in a directory to PNG.
    
    Args:
        input_dir (str): Directory containing EPS files
        output_dir (str, optional): Directory for output PNG files. If None, uses same directory as input
        dpi (int, optional): Resolution for output PNGs. Defaults to 300
    """
    input_dir = Path(input_dir)
    
    # If no output directory specified, use input directory
    if output_dir is None:
        output_dir = input_dir
    output_dir = Path(output_dir)
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all EPS files
    eps_files = list(input_dir.glob('*.eps'))
    
    if not eps_files:
        print(f"No EPS files found in {input_dir}")
        return
    
    print(f"Found {len(eps_files)} EPS files to convert")
    
    # Convert each file
    for eps_file in eps_files:
        output_path = output_dir / eps_file.with_suffix('.png').name
        convert_eps_to_png(eps_file, output_path, dpi)

# Example usage
if __name__ == "__main__":
    # Convert a single file
    #convert_eps_to_png("nested_shapes.eps")
    
    # Convert all files in a directory
    batch_convert_directory("examples")
