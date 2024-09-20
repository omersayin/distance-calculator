{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b8d0ef40-c9fa-4189-a3e7-0314f927835a",
   "metadata": {},
   "outputs": [],
   "source": [
    "i=5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4e640743-2d95-49b5-9da2-1abea708798d",
   "metadata": {},
   "outputs": [],
   "source": [
    "j=5\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2ae8f9e1-9679-43c2-ad88-7c6e868b127d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "i==j\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "23108103-49ab-4347-84c0-bde32a3451ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "i=10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "14b62543-c3ef-4cff-b5fd-ac0efc106e43",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "i==j"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "71c738ce-8ec2-4f7f-9dd3-d0eb3bec88d2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"Elma\"==\"Elma\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "94f54fd6-732b-4b7a-9c94-8d898ca5bd80",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"Elma\"==\"Armut\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c1eef6a0-02c2-4818-af20-568b4e45b6f3",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Elma' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[15], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m A\u001b[38;5;241m=\u001b[39mElma\n",
      "\u001b[1;31mNameError\u001b[0m: name 'Elma' is not defined"
     ]
    }
   ],
   "source": [
    "A=Elma"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "87856aa3-ea7d-4f38-8add-124b4b7ea37d",
   "metadata": {},
   "outputs": [],
   "source": [
    "A=\"Elma\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "51084820-b87f-4f86-ad68-587f9ec04d54",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"ab\" < \"fgrf\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5b191921-6dae-4747-80f1-978e6967b802",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"ab\" > \"fege\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "810d70f7-5c4a-43b0-b86f-238c0d3807bb",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "'(' was never closed (1366125202.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[25], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    x = int(input(\"Bir sayi girin:\")\u001b[0m\n\u001b[1;37m           ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m '(' was never closed\n"
     ]
    }
   ],
   "source": [
    "x = int(input(\"Bir sayi girin:\")\n",
    "if x % 2 == 0:\n",
    "        print(\"sayiniz cift sayi\")\n",
    "print(\"programiniz sona ulasti\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "762ff13d-e63c-49e2-bf14-c1ecb9e0bf70",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "'(' was never closed (2336845105.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[27], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    x = int(input(\"Bir sayi girin:\")\u001b[0m\n\u001b[1;37m           ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m '(' was never closed\n"
     ]
    }
   ],
   "source": [
    "x = int(input(\"Bir sayi girin:\")\n",
    "if x % 2 == 0:\n",
    "        print(\"sayiniz cift sayi\")\n",
    "print(\"programiniz sona ulasti\")\n",
    "\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "eaf09ee8-9148-422f-98ba-ed6b79dd08b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Bir sayi girin: 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sayiniz cift sayi\n",
      "programiniz sona ulasti\n"
     ]
    }
   ],
   "source": [
    "x = int(input(\"Bir sayi girin:\"))\n",
    "if x % 2 == 0:\n",
    "        print(\"sayiniz cift sayi\")\n",
    "print(\"programiniz sona ulasti\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "d815772f-c0b2-4c86-8297-256d3761b0a1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Bir sayi girin: 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "programiniz sona ulasti\n"
     ]
    }
   ],
   "source": [
    "x = int(input(\"Bir sayi girin:\"))\n",
    "if x % 2 == 0:\n",
    "        print(\"sayiniz cift sayi\")\n",
    "\n",
    "if x % 3 ==1:\n",
    "    print(\"sayiniz tek sayi\")\n",
    "print(\"programiniz sona ulasti\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "542ac10d-7d3f-46e7-99d9-b3820dedb23b",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "expected ':' (2638094076.py, line 5)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[33], line 5\u001b[1;36m\u001b[0m\n\u001b[1;33m    else x % 3 ==1:\u001b[0m\n\u001b[1;37m         ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m expected ':'\n"
     ]
    }
   ],
   "source": [
    "x = int(input(\"Bir sayi girin:\"))\n",
    "if x % 2 == 0:\n",
    "        print(\"sayiniz cift sayi\")\n",
    "\n",
    "else x % 3 ==1:\n",
    "    print(\"sayiniz tek sayi\")\n",
    "print(\"programiniz sona ulasti\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "094a8a85-fb3a-4df3-b432-bb08990779b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Bir sayi girin: 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sayiniz tek sayi\n",
      "programiniz sona ulasti\n"
     ]
    }
   ],
   "source": [
    "x = int(input(\"Bir sayi girin:\"))\n",
    "if x % 2 == 0:\n",
    "        print(\"sayiniz cift sayi\")\n",
    "else:\n",
    "    print(\"sayiniz tek sayi\")\n",
    "print(\"programiniz sona ulasti\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "3d8329b9-8e63-46fa-a427-1344cad11c9f",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax. Perhaps you forgot a comma? (2529491345.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[39], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    x = int(input(\"\"bir sayi girin))\u001b[0m\n\u001b[1;37m                  ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax. Perhaps you forgot a comma?\n"
     ]
    }
   ],
   "source": [
    "x = int(input(\"\"bir sayi girin))\n",
    "\n",
    "if x < 10:\n",
    "  print(\"sayi 10'dan kucuk\")\n",
    "\n",
    "elif x ==10:\n",
    "  print(\"sayi 10'dan buyuk\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "030d9278-8641-4f72-9528-1f8e2c07e90b",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unterminated string literal (detected at line 1) (2318951904.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[41], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    x = int(input(bir sayi girin\"))\u001b[0m\n\u001b[1;37m                                ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m unterminated string literal (detected at line 1)\n"
     ]
    }
   ],
   "source": [
    "x = int(input(bir sayi girin\"))\n",
    "\n",
    "if x < 10:\n",
    "  print(\"sayi 10'dan kucuk\")\n",
    "\n",
    "elif x ==10:\n",
    "  print(\"sayi 10'dan buyuk\")\n",
    "\n",
    "else:\n",
    "    print(\"sayi 10 dan buyuk\") \n",
    "              \n",
    "print(\"programiniz sona ulasi\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "70a61597-3360-490d-9db0-5a7519bf8eba",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unterminated string literal (detected at line 1) (4012066033.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[43], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    x = int(input(bir sayi girin\"))\u001b[0m\n\u001b[1;37m                                ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m unterminated string literal (detected at line 1)\n"
     ]
    }
   ],
   "source": [
    "x = int(input(bir sayi girin\"))\n",
    "\n",
    "if x < 10:\n",
    "  print(\"sayi 10'dan kucuk\")\n",
    "\n",
    "elif x == 10:\n",
    "  print(\"sayi 10'dan buyuk\")\n",
    "\n",
    "else:\n",
    "   print(\"sayi 10 dan buyuk\") \n",
    "              \n",
    "print(\"programiniz sona ulasi\")\n",
    "              "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "8de9e67b-6bb9-4de0-ac79-40d9415c0296",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "bir sayi girin 11\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sayi 10 dan buyuk\n",
      "programiniz sona ulasi\n"
     ]
    }
   ],
   "source": [
    "x = int(input(\"bir sayi girin\"))\n",
    "\n",
    "if x < 10:\n",
    "  print(\"sayi 10'dan kucuk\")\n",
    "\n",
    "elif x == 10:\n",
    "  print(\"sayi 10'dan buyuk\")\n",
    "\n",
    "else:\n",
    "   print(\"sayi 10 dan buyuk\") \n",
    "              \n",
    "print(\"programiniz sona ulasi\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d68167b-c051-487a-9d58-57eff6009ca9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
