import time


def deco_start_end(func):
  """
  処理の開始と終わりをログ出力するデコレーター
  """
  def wrapper(*args, **kwargs):
    print("---start---")
    func(*args, **kwargs)
    print("---end---")
  return wrapper


def deco_processing_time(func):
  """
  処理時間を計測し、ログ出力するデコレーター
  """
  def wrapper(*args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    result_time = end_time - start_time
    # 処理時間を読みやすい形式で表示
    if result_time < 0.001:  # 1ミリ秒未満
        print(f"処理時間: {result_time * 1000000:.2f} μs")
    elif result_time < 1.0:  # 1秒未満
        print(f"処理時間: {result_time * 1000:.2f} ms")
    else:  # 1秒以上
        print(f"処理時間: {result_time:.2f} s")

  return wrapper

@deco_start_end
@deco_processing_time
def main():
    print("Hello, World!")


if __name__ == "__main__":
    # source venv/bin/activate
    # python checker/decorator.py
    # deactivate
    main()
