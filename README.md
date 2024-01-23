| Algorithm          | Real Substring (Text 1) | Fake Substring (Text 1) | Real Substring (Text 2) | Fake Substring (Text 2) |
| ------------------ | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| Boyer-Moore        | 0.008710 sec            | 0.539059 sec            | 0.003194 sec            | 0.700810 sec            |
| Knuth-Morris-Pratt | 0.005066 sec            | 1.287703 sec            | 0.003164 sec            | 1.949856 sec            |
| Rabin-Karp         | 0.005156 sec            | 3.049817 sec            | 0.002786 sec            | 3.761100 sec            |
| String-Search      | 0.145096 sec            | 0.001653 sec            | 0.184933 sec            | 0.002083 sec            |

![Alt text](/images/image.png) ![Alt text](/images/image-1.png)
| Algorithm | Real Substring (Text 1) | Fake Substring (Text 1) | Real Substring (Text 2) | Fake Substring (Text 2) |
| ------------------ | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| Boyer-Moore | 0.016007 sec | - | 0.004618 sec | - |
| Knuth-Morris-Pratt | 0.009685 sec | - | 0.002512 sec | - |
| Rabin-Karp | 0.002980 sec | - | 0.001604 sec | - |
| String-Search | 0.101317 sec | - | 0.162526 sec | - |

| Algorithm          | Real Substring (Text 1) | Fake Substring (Text 1) | Real Substring (Text 2) | Fake Substring (Text 2) |
| ------------------ | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| Boyer-Moore        | -                       | 0.591704 sec            | -                       | 0.600072 sec            |
| Knuth-Morris-Pratt | -                       | 1.208102 sec            | -                       | 2.058599 sec            |
| Rabin-Karp         | -                       | 2.940864 sec            | -                       | 4.205234 sec            |
| String-Search      | -                       | 0.001672 sec            | -                       | 0.002048 sec            |
