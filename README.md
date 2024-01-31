Real & Fake Pattern.
| Algorithm | Real Substring (Text 1) | Fake Substring (Text 1) | Real Substring (Text 2) | Fake Substring (Text 2) |
|--------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Boyer-Moore | 0.000012 sec | 0.000318 sec | 0.000012 sec | 0.000444 sec |
| Knuth-Morris-Pratt | 0.000006 sec | 0.000654 sec | 0.000006 sec | 0.000929 sec |
| Rabin-Karp | 0.000012 sec | 0.001496 sec | 0.000012 sec | 0.002212 sec |
| String-Search | 0.000112 sec | 0.000003 sec | 0.000112 sec | 0.000002 sec |

![Alt text](/images/image-0.png)![Alt text](/images/image-1.png)

Only Real Pattern.
| Algorithm | Real Substring (Text 1) | Fake Substring (Text 1) | Real Substring (Text 2) | Fake Substring (Text 2) |
|--------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Boyer-Moore | 0.000046 sec | - | 0.000046 sec | - |
| Knuth-Morris-Pratt | 0.000020 sec | - | 0.000020 sec | - |
| Rabin-Karp | 0.000026 sec | - | 0.000026 sec | - |
| String-Search | 0.000383 sec | - | 0.000383 sec | - |

![Alt text](/images/image-2.png)![Alt text](/images/image-3.png)

Only Fake Pattern.
| Algorithm | Real Substring (Text 1) | Fake Substring (Text 1) | Real Substring (Text 2) | Fake Substring (Text 2) |
|--------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Boyer-Moore | - | 0.002874 sec | - | 0.002798 sec |
| Knuth-Morris-Pratt | - | 0.003539 sec | - | 0.004640 sec |
| Rabin-Karp | - | 0.009259 sec | - | 0.008551 sec |
| String-Search | - | 0.000020 sec | - | 0.000012 sec |

![Alt text](/images/image-4.png)![Alt text](/images/image-5.png)
