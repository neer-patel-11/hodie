# test_mcp_tools.py
import asyncio
import sys
from graph.tools.tools import (
    initialize_mcp,
    cleanup_mcp,
    get_tools,
    execute_shell_command,
    add_numbers,
)

async def test_initialization():
    """Test MCP initialization"""
    print("\n" + "="*60)
    print("TEST 1: MCP Initialization")
    print("="*60)
    
    try:
        tools = await initialize_mcp()
        if tools:
            print(f"✓ SUCCESS: Initialized with {len(tools)} MCP tools")
            return True
        else:
            print("✗ FAILED: No tools returned")
            return False
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False

async def test_get_tools():
    """Test the get_tools function"""
    print("\n" + "="*60)
    print("TEST 2: Get All Tools")
    print("="*60)
    
    try:
        tools = await get_tools()
        print(f"✓ Found {len(tools)} total tools:")
        for tool in tools:
            print(f"  - {tool.name}: {tool.description}")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False

async def test_add_numbers():
    """Test the basic add_numbers tool"""
    print("\n" + "="*60)
    print("TEST 3: Add Numbers Tool (Non-MCP)")
    print("="*60)
    
    try:
        result = add_numbers.invoke({"a": 5, "b": 3})
        expected = 8
        
        if result == expected:
            print(f"✓ SUCCESS: 5 + 3 = {result}")
            return True
        else:
            print(f"✗ FAILED: Expected {expected}, got {result}")
            return False
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False

async def test_get_username():
    """Test the get_windows_username tool"""
    print("\n" + "="*60)
    print("TEST 4: Get Windows Username")
    print("="*60)
    
    try:
        result = await get_windows_username.ainvoke({})
        print(f"✓ SUCCESS: {result}")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False

async def test_execute_command():
    """Test the execute_shell_command tool"""
    print("\n" + "="*60)
    print("TEST 5: Execute Shell Command")
    print("="*60)
    
    # Safe commands to test on different platforms
    test_commands = {
        "win32": "echo Hello from Windows",
        "linux": "echo Hello from Linux",
        "darwin": "echo Hello from macOS",
    }
    
    platform = sys.platform
    command = test_commands.get(platform, "echo Hello")
    
    try:
        print(f"Executing: {command}")
        result = await execute_shell_command.ainvoke({"command": command})
        print(f"✓ Result:\n{result}")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False

async def test_tool_caching():
    """Test that tools are properly cached"""
    print("\n" + "="*60)
    print("TEST 6: Tool Caching")
    print("="*60)
    
    try:
        tools1 = await get_tools()
        tools2 = await get_tools()
        
        if tools1 is tools2:
            print("✓ SUCCESS: Tools are cached (same object)")
            return True
        else:
            print("✗ WARNING: Tools not cached (different objects)")
            return False
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False

async def run_all_tests():
    """Run all tests in sequence"""
    print("\n" + "="*60)
    print("RUNNING ALL MCP TOOL TESTS")
    print("="*60)
    
    results = []
    
    # Test 1: Initialization
    results.append(("Initialization", await test_initialization()))
    
    # Test 2: Get tools
    results.append(("Get Tools", await test_get_tools()))
    
    # Test 3: Add numbers (basic tool)
    results.append(("Add Numbers", await test_add_numbers()))

    
    # Test 5: Execute command (MCP tool)
    results.append(("Execute Command", await test_execute_command()))
    
    # Test 6: Tool caching
    results.append(("Tool Caching", await test_tool_caching()))
    
    # Cleanup
    await cleanup_mcp()
    
    # Print summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{status}: {test_name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    print("="*60)

async def interactive_test():
    """Interactive testing mode"""
    print("\n" + "="*60)
    print("INTERACTIVE TEST MODE")
    print("="*60)
    
    await initialize_mcp()
    tools = await get_tools()
    
    print("\nAvailable tools:")
    for i, tool in enumerate(tools, 1):
        print(f"{i}. {tool.name}: {tool.description}")
    
    while True:
        print("\n" + "-"*60)
        print("Commands:")
        print("  1-{}: Test a specific tool".format(len(tools)))
        print("  'list': Show tools again")
        print("  'quit': Exit")
        print("-"*60)
        
        choice = input("\nEnter command: ").strip().lower()
        
        if choice == 'quit':
            break
        elif choice == 'list':
            for i, tool in enumerate(tools, 1):
                print(f"{i}. {tool.name}: {tool.description}")
            continue
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(tools):
                tool = tools[idx]
                print(f"\nTesting: {tool.name}")
                
                # Simple test cases for each tool
                if tool.name == "add_numbers":
                    result = tool.invoke({"a": 10, "b": 20})
                    print(f"Result: {result}")
                elif tool.name == "get_windows_username":
                    result = await tool.ainvoke({})
                    print(f"Result: {result}")
                elif tool.name == "execute_shell_command":
                    cmd = input("Enter command to execute: ")
                    result = await tool.ainvoke({"command": cmd})
                    print(f"Result: {result}")
                elif tool.name == "duckduckgo_search":
                    query = input("Enter search query: ")
                    result = await tool.ainvoke({"query": query})
                    print(f"Result: {result}")
                else:
                    print("No test implementation for this tool")
            else:
                print("Invalid tool number")
        except ValueError:
            print("Invalid input")
        except Exception as e:
            print(f"Error: {e}")
    
    await cleanup_mcp()
    print("\nExiting interactive mode...")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Test MCP tools")
    parser.add_argument(
        "--mode",
        choices=["all", "interactive"],
        default="all",
        help="Test mode: 'all' for automated tests, 'interactive' for manual testing"
    )
    
    args = parser.parse_args()
    
    if args.mode == "all":
        asyncio.run(run_all_tests())
    else:
        asyncio.run(interactive_test())