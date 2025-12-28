from utils.calculate_utils import calculate_sum

def main() -> None:
  message: str = "Hello, World!"
  print(message)

  sum = calculate_sum(1, 2)
  print(sum)

if __name__ == "__main__":
  # source venv/bin/activate
  # python main.py
  # mypy main.py
  # deactivate
  main()
