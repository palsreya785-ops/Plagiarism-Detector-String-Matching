from algorithms.naive import naive_search
from algorithms.kmp import kmp_search
from algorithms.rabin_karp import rabin_karp

text = "data structures and algorithms"
pattern = "algorithms"

print("Naive:", naive_search(text, pattern))
print("KMP:", kmp_search(text, pattern))
print("Rabin-Karp:", rabin_karp(text, pattern))