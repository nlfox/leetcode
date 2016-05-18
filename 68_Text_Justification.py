class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        word_lens = [len(i) for i in words]
        word_num = len(words)
        last = 0
        t_sum = 0
        lines = []
        line_nums = []
        res = []
        for i in xrange(word_num):
            if (t_sum + word_lens[i] <= maxWidth):
                t_sum += word_lens[i] + 1
            else:
                lines.append(words[last: i])
                line_nums.append(t_sum - 1)
                last = i
                t_sum = word_lens[i] + 1

        lines.append(words[last: word_num])
        line_nums.append(t_sum - 1)
        print lines, line_nums
        for idx, line in enumerate(lines[0:-1]):
            line_word_num = len(line)
            to_fill = maxWidth - line_nums[idx]
            if line_word_num == 1:
                res.append(''.join(line) + " " * to_fill)
                continue
            if to_fill % (line_word_num - 1) == 0:
                if line_word_num > 1:
                    res.append(((to_fill / (line_word_num - 1) + 1) * ' ').join(line))
                else:
                    res.append(''.join(line) + " " * to_fill)
            else:
                def_space = to_fill / (line_word_num - 1) + 1
                tl = (def_space * ' ').join(line)
                if len(tl) != maxWidth:
                    left = maxWidth - len(tl)
                    i = 0
                    n = len(lines[idx][i])
                    while left > 0:
                        tl = tl[0:n] + " " + tl[n:]
                        i += 1
                        n += len(lines[idx][i]) + def_space + 1
                        left -= 1
                    res.append(tl)
                else:
                    res.append(tl)
        res.append(' '.join(lines[-1]) + " " * (maxWidth - line_nums[-1]))
        return res


print Solution().fullJustify(["a", "b", "c", "d", "e"], 1)
