# ============================================================
# Python 綜合練習範例
# 涵蓋：變數、函式、類別、串列推導、例外處理、檔案操作
# ============================================================

# ── 1. 基本資料型別與運算 ────────────────────────────────────
name = "台北"
temperature = 36.5
is_summer = True

print(f"城市：{name}，氣溫：{temperature}°C，夏天：{is_summer}")


# ── 2. 串列與串列推導 ────────────────────────────────────────
scores = [85, 92, 78, 61, 95, 70, 88]

# 找出及格（>= 60）且高分（>= 80）的成績
high_scores = [s for s in scores if s >= 80]
pass_scores = [s for s in scores if s >= 60]

print(f"\n所有成績：{scores}")
print(f"高分（≥80）：{high_scores}")
print(f"及格（≥60）：{pass_scores}")
print(f"平均分數：{sum(scores) / len(scores):.2f}")


# ── 3. 函式與預設參數 ────────────────────────────────────────
def greet(name: str, lang: str = "zh") -> str:
    """根據語言回傳問候語"""
    messages = {
        "zh": f"你好，{name}！",
        "en": f"Hello, {name}!",
        "jp": f"こんにちは、{name}！",
    }
    return messages.get(lang, f"Hi, {name}!")


print("\n── 多語問候 ──")
for lang in ["zh", "en", "jp", "fr"]:
    print(greet("世界", lang))


# ── 4. 字典操作 ──────────────────────────────────────────────
students = {
    "小明": 85,
    "小華": 92,
    "小美": 78,
    "小強": 61,
}

print("\n── 學生成績 ──")
for student, score in sorted(students.items(), key=lambda x: x[1], reverse=True):
    grade = "優" if score >= 90 else "良" if score >= 80 else "可" if score >= 70 else "待加強"
    print(f"  {student}：{score} 分 ({grade})")


# ── 5. 類別與物件導向 ────────────────────────────────────────
class BankAccount:
    """簡易銀行帳戶"""

    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self._balance = balance
        self._history: list[str] = []

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("存款金額必須大於 0")
        self._balance += amount
        self._history.append(f"存款 +{amount:.0f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("提款金額必須大於 0")
        if amount > self._balance:
            raise ValueError(f"餘額不足（現有 {self._balance:.0f} 元）")
        self._balance -= amount
        self._history.append(f"提款 -{amount:.0f}")

    @property
    def balance(self) -> float:
        return self._balance

    def show_history(self) -> None:
        print(f"\n── {self.owner} 的帳戶明細 ──")
        for record in self._history:
            print(f"  {record}")
        print(f"  目前餘額：{self._balance:.0f} 元")


# ── 6. 例外處理 ──────────────────────────────────────────────
print("\n── 銀行帳戶操作 ──")
account = BankAccount("小明", 1000)

operations = [
    ("deposit", 500),
    ("withdraw", 200),
    ("withdraw", 2000),   # 預期會失敗
    ("deposit", -100),    # 預期會失敗
]

for action, amount in operations:
    try:
        if action == "deposit":
            account.deposit(amount)
            print(f"存款 {amount} 元：成功")
        elif action == "withdraw":
            account.withdraw(amount)
            print(f"提款 {amount} 元：成功")
    except ValueError as e:
        print(f"操作失敗：{e}")

account.show_history()


# ── 7. 產生器（Generator） ───────────────────────────────────
def fibonacci(n: int):
    """產生前 n 個費波那契數"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


fib_list = list(fibonacci(10))
print(f"\n費波那契數列（前10項）：{fib_list}")


# ── 8. 簡易統計函式 ──────────────────────────────────────────
def statistics(data: list[float]) -> dict:
    """回傳基本統計資料"""
    sorted_data = sorted(data)
    n = len(sorted_data)
    mean = sum(sorted_data) / n
    median = (
        sorted_data[n // 2]
        if n % 2 == 1
        else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    )
    variance = sum((x - mean) ** 2 for x in sorted_data) / n
    return {
        "數量": n,
        "最小值": sorted_data[0],
        "最大值": sorted_data[-1],
        "平均值": round(mean, 2),
        "中位數": median,
        "標準差": round(variance ** 0.5, 2),
    }


print("\n── 成績統計 ──")
stats = statistics(scores)
for key, value in stats.items():
    print(f"  {key}：{value}")
