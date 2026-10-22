import os
import subprocess
import sys


def run_command(cmd_str):
  args = cmd_str.split()
  if not args:
    return

  if args[0] == "cd":
    try:
      os.chdir(args[1] if len(args) > 1 else os.path.expanduser("~"))
    except Exception as e:
      print(f"cd: {e}")
    return

  if args[0] == "exit":
    sys.exit(0)

  infile = None
  outfile = None
  clean_args = []

  i = 0
  while i < len(args):
    if args[i] == "<":
      infile = args[i + 1]
      i += 2
    elif args[i] == ">":
      outfile = args[i + 1]
      i += 2
    else:
      clean_args.append(args[i])
      i += 1

  in_fh = open(infile, "r") if infile else None
  out_fh = open(outfile, "w") if outfile else None

  try:
    subprocess.run(clean_args, stdin=in_fh, stdout=out_fh)
  except FileNotFoundError:
    print(f"shell: command not found: {clean_args[0]}")
  finally:
    if in_fh:
      in_fh.close()
    if out_fh:
      out_fh.close()


def run_pipeline(line):
  commands = [c.strip() for c in line.split("|")]

  if len(commands) == 1:
    run_command(commands[0])
    return

  procs = []
  prev_stdout = None

  for i, cmd in enumerate(commands):
    args = cmd.split()
    if not args:
      continue

    stdin = prev_stdout
    stdout = (
        subprocess.PIPE if i < len(commands) - 1 else None
    )

    try:
      p = subprocess.Popen(args, stdin=stdin, stdout=stdout)
      procs.append(p)
      prev_stdout = p.stdout
    except FileNotFoundError:
      print(f"shell: command not found: {args[0]}")
      break

  for p in procs:
    p.wait()


def main():
  while True:
    try:
      line = input("$ ").strip()
      if line:
        run_pipeline(line)
    except (KeyboardInterrupt, EOFError):
      print()
      break


if __name__ == "__main__":
  main()