# SEARCH ALGORITM

Real & Fake Pattern.
| Algorithm | Real Substring (Text 1) | Fake Substring (Text 1) | Real Substring (Text 2) | Fake Substring (Text 2) |
|--------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Boyer-Moore | 0.000012 sec | 0.000318 sec | 0.000012 sec | 0.000444 sec |
| Knuth-Morris-Pratt | 0.000006 sec | 0.000654 sec | 0.000006 sec | 0.000929 sec |
| Rabin-Karp | 0.000012 sec | 0.001496 sec | 0.000012 sec | 0.002212 sec |
| String-Search | 0.000112 sec | 0.000003 sec | 0.000112 sec | 0.000002 sec |

![Alt text](src/assets/images/image-0.png)![Alt text](src/assets/images/image-1.png)

Only Real Pattern.
| Algorithm | Real Substring (Text 1) | Fake Substring (Text 1) | Real Substring (Text 2) | Fake Substring (Text 2) |
|--------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Boyer-Moore | 0.000046 sec | - | 0.000046 sec | - |
| Knuth-Morris-Pratt | 0.000020 sec | - | 0.000020 sec | - |
| Rabin-Karp | 0.000026 sec | - | 0.000026 sec | - |
| String-Search | 0.000383 sec | - | 0.000383 sec | - |

![Alt text](src/assets/images/image-2.png)![Alt text](src/assets/images/image-3.png)

Only Fake Pattern.
| Algorithm | Real Substring (Text 1) | Fake Substring (Text 1) | Real Substring (Text 2) | Fake Substring (Text 2) |
|--------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Boyer-Moore | - | 0.002874 sec | - | 0.002798 sec |
| Knuth-Morris-Pratt | - | 0.003539 sec | - | 0.004640 sec |
| Rabin-Karp | - | 0.009259 sec | - | 0.008551 sec |
| String-Search | - | 0.000020 sec | - | 0.000012 sec |

![Alt text](src/assets/images/image-4.png)![Alt text](src/assets/images/image-5.png)

# SORT ALGORITM

| Data Size |  Merge Sort | Insertion Sort |     TimSort |
| --------: | ----------: | -------------: | ----------: |
|       100 |  6.8939e-05 |    6.96897e-06 | 1.91102e-06 |
|       500 | 0.000376264 |     2.5464e-05 | 1.71701e-06 |
|      1000 | 0.000791304 |     4.4269e-05 | 3.01696e-06 |
|      3000 |  0.00277844 |    0.000127299 | 7.24697e-06 |

![Alt text](src/assets/images/image-6.png)

# BAG ALGORITM

| Amount | Greedy Result                           | Dynamic Result                          |
| -----: | :-------------------------------------- | :-------------------------------------- |
|     87 | {50: 1, 25: 1, 10: 1, 2: 1}             | {50: 1, 25: 1, 10: 1, 2: 1}             |
|    143 | {50: 2, 25: 1, 10: 1, 5: 1, 2: 1, 1: 1} | {50: 2, 25: 1, 10: 1, 5: 1, 2: 1, 1: 1} |
|    289 | {50: 5, 25: 1, 10: 1, 2: 2}             | {50: 5, 25: 1, 10: 1, 2: 2}             |
|    498 | {50: 9, 25: 1, 10: 2, 2: 1, 1: 1}       | {50: 9, 25: 1, 10: 2, 2: 1, 1: 1}       |
|   1023 | {50: 20, 10: 2, 2: 1, 1: 1}             | {50: 20, 10: 2, 2: 1, 1: 1}             |
|   3764 | {50: 75, 10: 1, 2: 2}                   | {50: 75, 10: 1, 2: 2}                   |

| Amount | Greedy Algorithm Time (s) | Dynamic Algorithm Time (s) |
| -----: | ------------------------: | -------------------------: |
|     87 |                1.4319e-05 |                0.000154262 |
|    143 |               7.53795e-06 |                 0.00026267 |
|    289 |               4.42803e-06 |                0.000485113 |
|    498 |               6.27298e-06 |                0.000905827 |
|   1023 |               5.67699e-06 |                 0.00198157 |
|   3764 |               5.16797e-06 |                 0.00854144 |

![Alt text](src/assets/images/image-7.png)
