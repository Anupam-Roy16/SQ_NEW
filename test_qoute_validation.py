import pytest
import qoute_validation as QV

@pytest.mark.parametrize("qoute,status", [
("""SQ 123 
we want  the   shelter of Lord 2 Jan 2078 Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja date: 28 Jun 2023 place: Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja
on 28 Jun 2023 place: Śrī Māyāpur, India
""",True),
("""SQ 123
we want  the   shelter of Lord Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja 
date: 28 Jun 2023 place: Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja 
date: 
28 Jun 2023 place: Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja date: 
28 Jun 2023 place: Śrī Māyāpur, India
""",True),

("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja on 28 Jun 2023 place: Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja on 
28 Jun 2023 place: Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja date: 28 Jun 2023 place: Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja
on 28 Jun 2023 place: Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus  feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja , 28 Jun 2023 place: Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja ,
 28 Jun 2023 place: Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja
 ,
 28 Jun 2023 place: Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja
 ,28 Jun 2023 place: Śrī Māyāpur, India
""",True),

("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja 28 Jun 2023 place: Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja 
28 Jun 2023 place: Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja on 28 Jun 2023 
place: Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja on 28 Jun 2023 
place: 
Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus  feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja on 28 Jun 2023 place: 
Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja on 28 Jun 2023 in Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja on 28 Jun 2023 
in Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus  feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja on 28 Jun 2023 in 
Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja on 28 Jun 2023 
in 
Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus  feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja on 28 Jun 2023 
Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja on 28 Jun 2023 Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus . SQ 123 . feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja on 28 Jun 2023 Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus  feet,and thus we can taste the nectar all the time. >>> Ref. His Holiness Jayapatākā Swami Mahārāja on 28 Jun 2023 Śrī Māyāpur, India
>>> Ref. His Holiness Jayapatākā Swami Mahārāja on 28 Jun 2023 Śrī Māyāpur, India
""",True),
("""SQ 123
we want  the   shelter of Lord  Caitanya’s lotus . feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārā date: 28 Jun 2023 Śrī Māyāpur, India
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja 28 Jun 2023
place: Śrī Māyāpur, 
India.""",True),

("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus >>> Ref. feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja 28 Jun 2023
place: Śrī Māyāpur, 
India.Hare Krishna Hare Krishna Krishna Krishna Hare Hare Hare Ram Hare Ram Ram Ram Hare Hare"""""""
""",True),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus >>> Ref. feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja 
place: Śrī Māyāpur, India date: 28 Jun 2023
Hare Krishna Hare Krishna Krishna Krishna Hare Hare Hare Ram Hare Ram Ram Ram Hare Hare"""""""
""",True),
("""SQ 123 
we want  the   shelter of Lord 2 Jan 2078 Caitanya’s lotus >>> Ref. feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja 28 Jun 2023
place: Śrī Māyāpur, India . Hare Krishna Hare Krishna Krishna Krishna
 Hare Hare Hare Ram Hare Ram Ram Ram Hare Hare . Iskon dhaka
""",True),
("""SQ 123 
we want  the   shelter of Lord 2 Jan 2078 Caitanya’s lotus >>> Ref. feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja date: 28  2023 place: Śrī Māyāpur, India.
""",False),
("""SQ 123 
we want  the   shelter of Lord 2 Jan 2078 Caitanya’s lotus  feet,and thus we can taste the nectar all the time. 
 His Holiness Jayapatākā Swami Mahārāja on 28 Jun 2023  in Śrī Māyāpur, India
""",False),
("""SQ 123 
we want  the   shelter of Lord Caitanya’s lotus >>> Ref. feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja on  place:
""",False),
("""we want  the   shelter of Lord  Caitanya’s lotus . SQ 123 . feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja on 28 Jun 2023 Śrī Māyāpur, India
""",False),
("""SQ 123
we want  the   shelter of Lord  Caitanya’s lotus  feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swam , Śrī Māyāpur, India date: 28 Jun 2023 
""",False),
("""SQ 123
we want  the   shelter of Lord  Caitanya’s lotus  feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārā , Śrī Māyāpur, India date: 28 Jun 2023 
""",False),
("""SQ 123 
we want  the   shelter of Lord  Caitanya’s lotus feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja
place: Śrī Māyāpur, India. 28 Jun 
2023""",False),

])



def test_Qoute_validty(qoute,status):
    qoute_object = QV.Qoute_validation(qoute)
    assert qoute_object.is_valid == status
