# Applying solid principles in a real application with python

## Introdução

SOLID é uma sigla para os primeiros cinco princípios do design orientado a objeto (OOD) criada por Robert C. Martin (também conhecido como Uncle Bob).

Esses princípios estabelecem algumas práticas que contribuem para o desenvolvimento de software com considerações de manutenção e extensão à medida que o projeto cresce. A adoção dessas práticas também pode contribuir para evitar problemas de código, refatoração de código e o desenvolvimento ágil e adaptativo de software.

SOLID significa:

- **S** - Single-responsibility Principle (Princípio da responsabilidade única)
- **O** - Open-closed Principle (Princípio do aberto-fechado)
- **L** - Liskov Substitution Principle (Princípio da substituição de Liskov)
- **I** - Interface Segregation Principle (Princípio da segregação de interfaces)
- **D** - Dependency Inversion Principle (Princípio da inversão de dependência)

## Princípio da responsabilidade única

> Uma classe deve ter um e apenas um motivo para mudar, o que significa que uma classe deve ter apenas uma função.

Como esse princípio nos ajuda a construir um software melhor?
Vejamos alguns de seus benefícios:

- **Teste** – Uma classe com uma responsabilidade terá muito menos casos de teste.
- **Menor acoplamento** – Menos funcionalidades em uma única classe terá menos dependências.
- **Organização** – Classes menores e bem organizadas são mais fáceis de pesquisar do que as monolíticas.

## Princípio do aberto-fechado

> Os objetos ou entidades devem estar abertos para extensão, mas fechados para modificação.

Ao fazer isso, nos impedimos de modificar o código existente e causar novos bugs em potencial em um aplicativo de outra forma feliz.

Claro, a única exceção à regra é ao corrigir bugs no código existente.

## Princípio da substituição de Liskov

> Seja q(x) uma propriedade demonstrável sobre objetos de x do tipo T. Então q(y) deve ser demonstrável para objetos y do tipo S onde S é um subtipo de T.

Simplificando, se a classe A for um subtipo da classe B , devemos ser capazes de substituir B por A sem interromper o comportamento do nosso programa.

## Princípio da segregação de interfaces

> Um cliente nunca deve ser forçado a implementar uma interface que ele não usa, ou os clientes não devem ser forçados a depender de métodos que não usam.

Ao fazer isso, podemos garantir que as classes de implementação só precisem se preocupar com os métodos que são de seu interesse.

## Princípio da inversão de dependência

> As entidades devem depender de abstrações, não de implementações. Ele declara que o módulo de alto nível não deve depender do módulo de baixo nível, mas devem depender de abstrações.

Dessa forma, ao invés de módulos de alto nível dependerem de módulos de baixo nível, ambos dependerão de abstrações.

## Conclusão

Neste artigo, os cinco princípios do Código SOLID foram-lhe apresentados. Projetos que aderem aos princípios SOLID podem ser compartilhados com colaboradores, estendidos, modificados, testados e refatorados com menos complicações.
