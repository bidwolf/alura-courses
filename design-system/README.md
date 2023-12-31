# Design system

Design systems são produtos escaláveis que servem outros produtos por meio de
suas bibliotecas de padrões, diretrizes, designers e desenvolvedores podem 
criar produtos digitais com mais agilidade e com mais agilidade.

Consumido indiretamente por outros produtos digitais, os design systems
versionam cada um dos diferentes tipos de elementos da interface do
produto, desde espaçamentos, fontes, cores até mesmo animações e sombras.

Além de tudo, design system é padrão, é documentação, ou mesmo orientação, é
o que liga design, desenvolvimento e produto em um único elo, e deve ser muito
bem pensado e planejado para que atenda não somente as necessidades do produto
mas também do usuário.
## O que compõe um Design System?

Um bom design system deve ser composto pelos seguintes elementos a seguir:

- `Guia de estilos`: Um guia que contém os elementos e componentes, suas
  interações e modo de uso. Sobre os elementos de tipografia, ícones, sombras,
  cores e etc.

- `Design Tokens` : Variáveis que representam todo tipo de característica de um
  design system.

- `Documentação` : Descrições sobre o motivo de existência de cada elemento de
  um design system, como em qual contexto utilizar cada botão, ou qual cor é
  utilizada para simbolizar um aviso, etc.

## Quais problemas eu resolvo com isso?

O Design System é um produto que assim como vários outros, têm o objetivo de
solucionar uma série de problemas significativos, abaixo estão alguns dos problemas
e as formas como o design system os soluciona.

Problema|Descrição|Solução
:---:|:---:|:---:
`Inconsistência visual`|É muito comum que o mesmo perca sua consistência visual, tanto por ser mantido por equipes diferentes, quanto por ser pensado de forma nova.|Garante que todos os **elementos de interface** mantenham uma aparência **consistente**,criando uma identidade visual unificada para a marca.
`Desperdício de tempo`| Retrabalho causado por criar novos **elementos de interface** a todo momento que o produto precisa.|Economiza tempo de designers e desenvolvedores **evitando duplicação de esforços** na criação de componentes e estilos.
`Atrasos no desenvolvimento`|Frequentemente causados por retrabalho, tanto quando se duplica código, quanto se cria variações de elementos similares.|Agiliza o processo de desenvolvimento, uma vez que os **componentes prontos para uso** podem ser **facilmente implementados**.
`Manutenção trabalhosa`|Imagine ter que dar manutenção no mesmo componente em 3 produtos digitais diferentes, sendo exatamente iguais, mas criados individualmente.|Facilita a manutenção contínua, uma vez que atualizações no design podem ser **aplicadas centralmente** e então **refletidas nos produtos digitais**.
`Problemas de escalabilidade`|Produtos criados de forma separadas, por mais parecidos que sejam são difíceis de escalar.|Ajuda a manter a **consistência** conforme os produtos/equipes crescem.
`Dificuldade na colaboração`|Designers, desenvolvedores, não se envolvem de forma única, sempre, demanda->entrega.|Facilita a colaboração entre designers e desenvolvedores, pois todos trabalham com um **conjunto comum de recursos**.
`Desafios de integração`|Produtos em plataformas diferentes sem um padrão a ser seguido podem ser difíceis de se integrar|Garante uma **integração mais suave** entre **sistemas e aplicativos**, pois os componentes são **projetados para funcionar juntos**.
`Má qualidade visual`|Imagine acessar um produto onde elementos que deveriam ser parecidos são completamente distintos uns dos outros, ou criados muitas vezes com pressa.|Mantém a qualidade visual dos produtos uma vez que os elementos são pensados com atenção aos detalhes.
`Comunicação eficaz`| - Combo-box? <br> - Não, o input de select!<br>- A cor blue-full-deep?<br>- Não, a cor blue-codelife-800.|Fornece uma **linguagem comum** para discutir design, evitando mal-entendidos.
`Falhas de usabilidade`|Bom, posso cadastrar mais de um email, é só colocar virgula depois! ***[FATAL ERROR 666]***.|Cria produtos em comum com **usabilidade testada** anteriormente.
`Desperdícios de recursos`|Tempo é dinheiro, e dinheiro é recurso|Reduz o desperdício de recursos financeiros e temporais no desenvolvimento de produtos.
`Mudanças constantes no design`|*We all know where is it going.*|Permite que as equipes de design **experimentem e inovem** dentro dos parâmetros do design system, mantendo a **consistência**.
`Treinamento de recrutas`|Bom pra dizer a verdade eu não sei que padrão você tem que seguir, siga seu coração bro.|implifica o treinamento de novos membros da equipe, pois eles podem seguir as **diretrizes do design system**.

## Inventário de interfaces

Um inventário de interfaces deve atender as necessidades dos produtos que vão consumi-lo de fato. Identificando estilos básico possíveis, altura de texto, cores, bordas, sombras, e o que mais vier!.

Em nosso caso, vamos utilizar o próprio figma para construção do inventário tomando como base um caso de exemplo criado pela rocketseat, cujo layout está contido no seguinte [link](https://www.figma.com/file/OstZl3BjIwfi0i4RWxSKYU/Ignite-Teams-(Community)-(Copy)?type=design&node-id=37-6&mode=design&viewport=0%252C0%252C1&t=toTGQVo0cZdJQZud-0)

### Cores

Abaixo se encontram todas as cores utilizadas no ignite-teams:
<div style="display:flex; flex-direction:column; gap:4px;width:100%;justify-content:center;align-items:center; font-size:17px; font-weight:500;">
<div style="width:300px;padding:1rem; background:#121214;color:#fff">#121214</div>
<div style="width:300px;padding:1rem; background:#202024;color:#fff">#202024</div>
<div style="width:300px;padding:1rem; background:#29292E;color:#fff">#29292E</div>
<div style="width:300px;padding:1rem; background:#323238;color:#fff">#323238</div>
<div style="width:300px;padding:1rem; background:#7C7C8A;color:#292900">#7C7C8A</div>
<div style="width:300px;padding:1rem; background:#C4C4CC;color:#292900">#C4C4CC</div>
<div style="width:300px;padding:1rem; background:#E1E1E6;color:#292900">#E1E1E6</div>
<div style="width:300px;padding:1rem; background:#FFFFFF;color:#292900">#FFFFFF</div>
<div style="width:300px;padding:1rem; background:#AA2834;color:#fff">#AA2834</div>
<div style="width:300px;padding:1rem; background:#CC2937;color:#fff">#CC2937</div>
<div style="width:300px;padding:1rem; background:#00B37E;color:#292900">#00B37E</div>
<div style="width:300px;padding:1rem; background:#00875F;color:#292900">#00875F</div>
<div style="width:300px;padding:1rem; background:#FBA94C;color:#292900">#FBA94C</div>
</div>

### Fontes

Roboto

### Paleta de cores utilizada no sistema
<div style="display:flex;gap:1rem; flex-direction:column">
<h3>Primary</h3>
<div style="display:flex;gap:1rem;">
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#6aebb6;color:#292900"></div>
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#2fd898;color:#292900"></div>
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#00CC8B;color:#292900"></div>
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#0abf81;color:#292900"></div>
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#024A35;color:#292900"></div>
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#004732;color:#292900"></div>
</div>
<h3>warning</h3>
<div style="display:flex;gap:1rem;">
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#fba94c;color:#292900"></div>
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#fa8c25;color:#292900"></div>
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#f4680c;color:#292900"></div>
<div style="width:100px;aspect-ratcolio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#d84607;or:#292900"></div>
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#b32b0a;color:#292900"></div>
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#91220f;color:#292900"></div>
</div>
<h3>Danger</h3>
<div style="display:flex;gap:1rem;">
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#f7aaaa;color:#292900"></div>
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#f17b7c;color:#292900"></div>
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#e84b51;color:#292900"></div>
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#cc2937;color:#292900"></div>
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#b21e2e;color:#292900"></div>
<div style="width:100px;aspect-ratio:1; display:flex; align-items:center;justify-content:center; font-size:24px; font-weight:600; background:#951c2d;color:#292900"></div>

</div>
</div>

## Tipografia

A tipografia é um elemento muito importante na construção de um produto digital.
Ela é quem transmite a mensagem que o seu produto deseja passar, por isso é
importante que seja bem pensada e bem cuidada para agradar a leitura e a mensagem
que seu produto deseja passar.

> No projeto atual, a escolha da fonte utilizada foi a fonte [montserrat](https://fonts.google.com/specimen/Montserrat).

Abaixo está o 