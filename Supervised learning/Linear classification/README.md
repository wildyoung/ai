# Linear classification

### when to use
It is used to predict the class of unseen data based on given data.
 
### Example situation
|  X  |  Y  |  Z  |
|:---:|:---:|:---:|
|  1  |  3  |  -1  |
|  3  | 10  |  1  |
|  5  |  8  |  -1 |
|  7  | 19  |  1  |
|  9  | 16  |  -1  |

<img width="480" alt="image" src="https://github.com/user-attachments/assets/aa42bb7f-70e5-4994-a2f4-274bac969883">




What is Z if X=10 and Y=25? 
<br></br>
                    
****
### How to predict?
Find the linear model 
Z=aX+bY+c that best predicts the target variable (Z) using the explanatory variable (X) and (Y) from the given data.
<br></br>

---

### What does it mean to make the best predictions?

It is about ensuring that when the explanatory variable (X) and (Y) are input into the linear model 
Z=aX+bY+c, the difference between the predicted target variable (Z) and the actual value is minimized.
<br></br>

---
### How are the values of a and b in the linear model Y=aX+b that minimize the error determined?
---
### step1 - Square the error

Linear model Z = aX+by+c

|  x  |  y  | z | prediction | error |
|:---:|:---:|---|:----------:|:-----:|
|  1  |  3  | -1 |     a+3b+c      |   a+3b+c - (-1)   |
|  3  | 10 | 1|     3a+10b+c    |  3a+10b+c -(+1)   |
|  5  | 8   | -1 |   5a+8b+c     |  5a+8b+c -(-1)   |
| 7   |19   |1 |    7a+19b+c    |  7a+19b+c-(+1)   |
|9    |16   |-1 |    9a+16b+c     |   9a+16b+c-(-1)   |


R = (a + 3b + c + 1)<sup>2</sup> + (3a + 10b + c - 1)<sup>2</sup> + (5a + 8b + c + 1)<sup>2</sup> + (7a + 19b + c - 1)<sup>2</sup> + (9a + 16b + c + 1)<sup>2</sup>



---
### step2 - Perform partial differentiation for each error

R = (a + 3b + c + 1)<sup>2</sup> + (3a + 10b + c - 1)<sup>2</sup> + (5a + 8b + c + 1)<sup>2</sup> + (7a + 19b + c - 1)<sup>2</sup> + (9a + 16b + c + 1)<sup>2</sup>

∂R(a)/∂a =0   
∂R(b)/∂b = 0  
∂R(c)/∂c = 0  

- Three equations derived from the expressions

---
### step3 - System of linear equations


---
### Result
<img width="469" alt="image" src="https://github.com/user-attachments/assets/c94880e3-ac8a-4e3e-a1ea-633d386936e2">


