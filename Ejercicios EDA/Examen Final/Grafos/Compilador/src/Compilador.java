import java.util.*;

public class Compilador
{
    HashMap<String, ArrayList<String>> dependencias;

    public Compilador(){
        dependencias = new HashMap<String, ArrayList<String>>();

        ArrayList<String> l1 = new ArrayList<String>();
        l1.add("PR2");
        l1.add("PR3");
        dependencias.put("PR1", l1);

        ArrayList<String> l2 = new ArrayList<String>();
        l2.add("PR5");
        l2.add("PR3");
        dependencias.put("PR2", l2);

        ArrayList<String> l15 = new ArrayList<String>();
        l15.add("PR5");
        l15.add("PR14");
        dependencias.put("PR15", l15);

        ArrayList<String> l3 = new ArrayList<String>();
        l3.add("PR5");
        dependencias.put("PR3", l3);

        ArrayList<String> l5 = new ArrayList<String>();
        l5.add("PR2");
        dependencias.put("PR5", l5);

        ArrayList<String> l14 = new ArrayList<String>();
        l14.add("PR25");
        dependencias.put("PR14", l14);

    }

    public boolean esValido(String prog)
    {
        boolean valido = true;
        Queue<String> porExaminar = (Queue<String>) new LinkedList<String>();
        HashSet<String> examinados = new HashSet<String>();

        if(dependencias.get(prog) == null)
        {
            valido = false;
        }
        else
        {
            porExaminar.add(prog);
            examinados.add(prog);
        }
        while(valido && !porExaminar.isEmpty())
        {
            String act = porExaminar.remove();

            if(dependencias.get(act) == null)
            {
                valido = false;
            }
            else
            {
                ArrayList<String> lista = dependencias.get(act);
                for(int i = 0; i < lista.size(); i++)
                {
                    if(!examinados.contains(lista.get(i)))
                    {
                        porExaminar.add(lista.get(i));
                        examinados.add(lista.get(i));
                    }
                    i++;
                }
            }

        }




        return valido;
    }
}
