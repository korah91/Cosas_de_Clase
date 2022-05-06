public int num_nodos(BTN<T> a, n)
{
  int suma = 0;
  if(n <= 1)
  {
    return 1;
  }
  else
  {
    if(a.left != null)
    {
      suma = suma + num_nodos(a.left, n-1);
    }
    if(a.right != null)
    {
      suma = suma + num_nodos(a.right, n-1)
    }
  }
  return suma
}
