# Reconhecimento Facial de Gado Bovino - TCC

O seguinte repositorio foi modificado tendo base o Cattle Recognition (https://github.com/eblancoh/cattle-recognition), e segue seu princípio de código aberto.

### Dataset
As imagens devem ser colocadas em pastas com os nomes dos animais dentro de uma pasta nomeada "dataset".

### Treinamento
Para realizar o treinamento deve-se utilizar o comando abaixo, subistituindo "test" pelo nome desejado para o treinamento.
```bash
$ python training.py --granja test --model resnet50 --epochs 20 --batch_size 30
```

### Gerar Gráficos do Treinamento
Para analisar o treinamento é possivel visualizar gráficos de accuracy e loss com o TensorBoard.
```bash
$ cd logs/folder/
$ tensorboard --logdir=./ --port 6006
```

### Testes
Para realizar um teste individual se utiliza o comando abaixo, passando o nome do treinamento e o path da imagem de teste.
```bash
$ python testing.py --granja test  --img "path/to/img"
```

O resultado é apresentado da seguinte forma:
```bash
{
    "class 0": score 0,
    "class 1": score 1,
    ...
    "class N": score N
}
```

## Licença 

Segundo o repositorio original o presente código é livre. Qualquer pessoa é livre de copiar, modificar, publicar, utilizar, compilar, vender, ou distribuir este software. 

"This is free and unencumbered software released into the public domain. Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."