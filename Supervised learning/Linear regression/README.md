# Linear Regression

### when to use
>It is used to predict the target variable (Y) for unknown explanatory variables (X) based on data about known explanatory variables (X) and the target variable (Y).
 
### Example situation
|  X  |  Y  |
|:---:|:---:|
|  <span style="color:blue">1</span>  |  <span style="color:green">3</span>  |
|  <span style="color:blue">3</span>  | <span style="color:green">10</span>  |
|  <span style="color:blue">5</span>  |  <span style="color:green">8</span>  |
|  <span style="color:blue">7</span>  | <span style="color:green">19</span>  |
|  <span style="color:blue">9</span>  | <span style="color:green">16</span>  | 

<img width="344" alt="image" src="https://github.com/user-attachments/assets/5eff651c-54fe-462f-b00a-99f824b3ca62">


What is Y if X=10? 
<br></br>
                    
****
### How to predict?
Find the linear model 
Y=aX+b that best predicts the target variable (Y) using the explanatory variable (X) from the given data.
<br></br>

---

### What does it mean to make the best predictions?

It is about ensuring that when the explanatory variable (X) is input into the linear model 
Y=aX+b, the difference between the predicted target variable (Y) and the actual value is minimized.
<br></br>

---
### How are the values of a and b in the linear model Y=aX+b that minimize the error determined?
---
### step1 - Square the error

Linear model Y=aX+b

|  x  |  y  | prediction | error |
|:---:|:---:|:----------------------:|:-------------------------:|
|  <span style="color:blue">1</span>  |  <span style="color:green">3</span>  |     a x <span style="color:blue">1</span> + b     |    a x <span style="color:blue">1</span> + b - <span style="color:green">3</span>    |
|  <span style="color:blue">3</span>  | <span style="color:green">10</span> |      a x <span style="color:blue">3</span> + b     |    a x <span style="color:blue">3</span> + b - <span style="color:green">10</span>    |
|  <span style="color:blue">5</span>  |  <span style="color:green">8</span>  |     a x <span style="color:blue">5</span> + b    |     a x <span style="color:blue">5</span> + b - <span style="color:green">8</span>    |
|  <span style="color:blue">7</span>  | <span style="color:green">19</span>  |      a x <span style="color:blue">7</span> + b     |    a x <span style="color:blue">7</span> + b - <span style="color:green">19</span>    |
|  <span style="color:blue">9</span>  | <span style="color:green">16</span>  |      a x <span style="color:blue">9</span> + b     |    a x <span style="color:blue">9</span> + b - <span style="color:green">16</span>    |


R =  (a x <span style="color:blue">1</span> + b - <span style="color:green">3</span>)<sup>2</sup> + (a x <span style="color:blue">3</span> + b - <span style="color:green">10</span>)<sup>2</sup> + (a x <span style="color:blue">5</span> + b - <span style="color:green">8</span>)<sup>2</sup> + (a x <span style="color:blue">7</span> + b - <span style="color:green">19</span>)<sup>2</sup> + (a x <span style="color:blue">9</span> + b - <span style="color:green">16</span>)<sup>2</sup> 

---
### step2 - Perform partial differentiation for each error

R =  (a x <span style="color:blue">1</span> + b - <span style="color:green">3</span>)<sup>2</sup> + (a x <span style="color:blue">3</span> + b - <span style="color:green">10</span>)<sup>2</sup> + (a x <span style="color:blue">5</span> + b - <span style="color:green">8</span>)<sup>2</sup> + (a x <span style="color:blue">7</span> + b - <span style="color:green">19</span>)<sup>2</sup> + (a x <span style="color:blue">9</span> + b - <span style="color:green">16</span>)<sup>2</sup> 

∂R₁(a)/∂a = 2a + 2b - 6  
∂R₂(a)/∂a = 18a + 6b - 60  
∂R₃(a)/∂a = 50a + 10b - 80  
∂R₄(a)/∂a = 98a + 14b - 266  
∂R₅(a)/∂a = 162a + 18b - 288  

Sum the derivatives with respect to a

330a + 50b - 700 = 0

---
∂R₁(b)/∂b = 2b + 2a - 6  
∂R₂(b)/∂b = 2b + 6a - 20  
∂R₃(b)/∂b = 2b + 10a - 16  
∂R₄(b)/∂b = 2b + 14a - 38  
∂R₅(b)/∂b = 2b + 18a - 32  

Sum the derivatives with respect to b

50a +10b - 112 = 0

---
### step3 - System of linear equations
 330a + 50b - 700 = 0  
 50a +10b - 112 = 0

5*(50a + 10b - 112) = 0  
250a + 50b - 560 = 0
<br></br>

   330a+50b=700  
250a+50b=560

80a = 140  
a = 1.75
b = 2.45

---
### Result
<img width="353" alt="image" src="https://github.com/user-attachments/assets/bede62fd-2d49-4ea7-bbf9-192c0f65b743">
