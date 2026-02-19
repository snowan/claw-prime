import os
import subprocess
import sys
import argparse

def run_command(cmd):
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    # Try baoyu-image-gen with Bun first (more robust than ts-node in this env)
    skill_path = "/Users/xiaowei.wan/.agents/skills/baoyu-image-gen/scripts/main.ts"
    cmd = ["bun", skill_path, "--prompt", args.prompt, "--image", args.output]
    
    print(f"Trying primary: {' '.join(cmd)}")
    result = run_command(cmd)
    
    # LOG OUTPUT FOR DEBUGGING
    if result.stdout: print(f"STDOUT: {result.stdout}")
    if result.stderr: print(f"STDERR: {result.stderr}")
    
    if result.returncode == 0:
        print("✅ Success with baoyu-image-gen")
        return

    if "429" in result.stderr or "quota" in result.stderr.lower():
        print("⚠️ Quota exceeded or error. Attempting fallback to Gemini Web...")
        # Fallback to Gemini Web API
        web_skill_path = "/Users/xiaowei.wan/.agents/skills/baoyu-danger-gemini-web/scripts/main.ts"
        fallback_cmd = ["bun", web_skill_path, "--prompt", args.prompt, "--image", args.output]
        result = run_command(fallback_cmd)
        
        if result.returncode == 0:
            print("✅ Success with baoyu-danger-gemini-web")
        else:
            print(f"❌ Fallback failed: {result.stderr}")
            sys.exit(1)
    else:
        print(f"❌ Generation failed: {result.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    main()
