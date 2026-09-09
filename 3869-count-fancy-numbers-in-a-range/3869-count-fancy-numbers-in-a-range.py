class Solution:
    def countFancy(self, l: int, r: int) -> int:
        def is_good(val: int) -> bool:
            s = str(val)
            if len(s) == 1:
                return True
            inc = all(s[i] < s[i + 1] for i in range(len(s) - 1))
            dec = all(s[i] > s[i + 1] for i in range(len(s) - 1))
            return inc or dec
        good_sums = {s for s in range(1, 136) if is_good(s)}
        goods = []
        def gen_inc(curr, last_digit):
            if curr > 0:
                goods.append(curr)
            for d in range(last_digit + 1, 10):
                gen_inc(curr * 10 + d, d)
        def gen_dec(curr, last_digit):
            if curr > 0:
                goods.append(curr)
            for d in range(last_digit - 1, -1, -1):
                gen_dec(curr * 10 + d, d)

        gen_inc(0, 0)
        gen_dec(0, 10)
        goods.append(0)
        goods = sorted(list(set(goods)))

        def count_good_sums(limit: int) -> int:
            if limit < 0:
                return 0
            s = str(limit)
            n = len(s)

            @lru_cache(None)
            def dp(idx: int, current_sum: int, is_tight: bool) -> int:
                if idx == n:
                    return 1 if current_sum in good_sums else 0

                upper_bound = int(s[idx]) if is_tight else 9
                total = 0
                for d in range(upper_bound + 1):
                    total += dp(idx + 1, current_sum + d, is_tight and (d == upper_bound))
                return total

            return dp(0, 0, True)

        def count_fancy_up_to(N: int) -> int:
            if N < 0:
                return 0
            total = count_good_sums(N)
            for g in goods:
                if g > N:
                    break
                if sum(map(int, str(g))) not in good_sums:
                    total += 1
            return total

        return count_fancy_up_to(r) - count_fancy_up_to(l - 1)