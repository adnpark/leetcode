# 다중 할당

2개 이상의 값을 2개 이상의 변수에 할당하는 것을 말함.

앞의 문제에서 이렇게 다중할당을 했는데, 가독성도 떨어지는데 왜 이렇게 했을까?

```python3
rev, rev.next, slow = slow, rev, slow.next
```

아래처럼 하면 깔끔할 것 같은데 왜 이렇게 안했을까?

```python3
fast = fast.next.next
rev, rev.next = slow, rev
slow = slow.next
```

하지만 이렇게 하면 rev와 rev.next가 동일한 참조를 가리키게 된다.
파이썬은 원시 타입이 존재하지 않고, 모든것이 객체이다. = 연산자를 이용한 할당은 값을 할당하는게 아니라 객체에 대한 참조를 할당한다. 다만 문자와 숫자의 경우 불변객체를 참조한다.

rev = 1, slow = 2 -> 3 이라고 가정해보자.

```python3
rev, rev.next, slow = slow, rev, slow.next
```

이 경우 우선 rev = 2->3, rev.next = 1 slow = 3 이 된다.
rev.next = 1 이 되었으므로, 최종적으로 rev = 2->1, slow = 3 이 된다.

- 다중할당을 하게 되면 이런 작업이 동시에 일어나기 때문에, 모든 작업은 하나의 트랜잭션으로 끝나게 된다.

하지만 아래와 같이 할당을 하게 되면

```python3
rev, rev.next = slow, rev
slow = slow.next
```

rev = 2->3, rev.next = 1 이 된다. 여기서 rev = 2->1이 되는데, 중요한점은 rev = slow 라는것. 따라서 slow는 2->3 이 아닌 2->1 이 되어서 결국 slow = slow.next의 결과는 slow = 1 이 된다.

그래서 이런 경우 반드시 다중할당을 통해서 문제를 풀어야 한다.
