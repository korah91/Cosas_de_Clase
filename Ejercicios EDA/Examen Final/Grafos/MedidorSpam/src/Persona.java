import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;

public class Persona {
    String nombre;
    int spamRecibidos = 0;
    ArrayList<Persona> contactos;

    public void enviarSpam()
    {
        Queue<Persona> porExaminar = (Queue<Persona>) new LinkedList<Persona>();
        HashSet<Persona> examinados = new HashSet<Persona>();

        Persona pers = new Persona();
        pers.nombre = this.nombre;
        pers.spamRecibidos = this.spamRecibidos;
        pers.contactos = this.contactos;

        porExaminar.add(pers);
        examinados.add(pers);

        while(!porExaminar.isEmpty())
        {

        }
        enviarSpam_aux(porExaminar, examinados);
    }

    private void enviarSpam_aux(Queue<Persona> porExaminar, HashSet<Persona> examinados)
    {
        


    }

// esto es aleatorio
    public boolean reenviar()
    {
        boolean bool = false;

        if(this.nombre.length() > 4)
        {
            bool = true;
        }
        return bool;
    }
}
