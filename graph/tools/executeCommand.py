import subprocess
from langchain_core.tools import tool

@tool
def execute_command(command: str, auto_confirm: bool = True) -> str:
    """
    Execute a shell command on the local Windows machine and return the output.
    
    Args:
        command: The shell command to execute (e.g., 'dir', 'echo hello', 'pip install package')
        auto_confirm: If True, automatically confirms prompts with 'y' (default: True)
    
    Returns:
        The command output as a string, or error message if execution fails.
    """
    # print("command :- ",command)
    print("Using cli tool")
    try:
        # On Windows, use shell=True for better compatibility with built-in commands
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30,
            shell=True,  # Required for Windows commands like 'dir', 'cd', etc.
            input='y\n' if auto_confirm else None  # Automatically send 'y' + newline
        )
        
        output = result.stdout
        if result.stderr:
            output += f"\nErrors/Warnings:\n{result.stderr}"
        
        if result.returncode != 0:
            output += f"\n[Command exited with code {result.returncode}]"
            
        return output if output else "[Command executed successfully with no output]"
        
    except subprocess.TimeoutExpired:
        return "Error: Command execution timed out after 30 seconds"
    except FileNotFoundError:
        return f"Error: Command not found"
    except Exception as e:
        return f"Error executing command: {str(e)}"