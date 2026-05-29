def eng_ko_p_u_chragan_elementni_toping(sana):
    return max(set(sana), key=sana.count)

sana = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(eng_ko_p_u_chragan_elementni_toping(sana))  # Chiqaradi: 4
```

```python
def eng_ko_p_u_chragan_elementni_toping(sana):
    return max(set(sana), key=sana.count)

sana = ['a', 'b', 'b', 'c', 'c', 'c', 'c']
print(eng_ko_p_u_chragan_elementni_toping(sana))  # Chiqaradi: 'c'
