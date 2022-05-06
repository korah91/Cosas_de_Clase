public LinkedList<T> listaOrdenada()
{
  LinkedList<T> lista = new LinkedList<T>;

  lista.insert(listaOrdenada(lista, this.left));
  lista.insert(this);
  lista.insert(listaOrdenada(lista, this.right));
}

private LinkedList<T> listaOrdenada(LinkedList<T> lista, BTN<T> a)
{
  if(a.left != null)
  {
    lista.insert(listaOrdenada(lista, a.left));
  }

  lista.insert(a);

  if(a.right != null)
  {
    lista.insert(listaOrdenada(lista, a.right));
  }
}
