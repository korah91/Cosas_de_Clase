import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Juego {

    Queue<Integer>[] jugadores;
    // Los colores de las fichas se representan por enteros ,donde las fichas
    // negras vienen dadas por el 0, y el resto de jugadores tendrán el color
    // correspondiente a la posición del jugador (es decir, el jugador 1 tendrá
    // fichas de valor 1, ...)
    Stack<Integer> mesa;
    int NUMJUGADORES = 6;

    public int juego(int n, ArrayList<Tirada> tiradas) {
        // pre: n es el número de fichas inicial de cada jugador
        // “tiradas” tiene los valores de los dados durante una partida
        // post: el resultado es el número del jugador ganador
        jugadores = new LinkedList[NUMJUGADORES];
        for (int i = 0; i < jugadores.length; i++)
            jugadores[i] = new LinkedList<Integer>();
        for (int i = 0; i < jugadores.length; i++)
            for (int j = 1; j <= n; j++)
                jugadores[i].add(i);

        boolean fin = false;
        int pos = 0;
        int num;

        mesa = new Stack<Integer>();

        while(!fin && pos < tiradas.size()-1 )
        {
            Tirada tir = tiradas.get(pos);
            if(tir.dado1 == 6)
            {
                fin = true;
            }
            else
            {
                if(tir.dado1 % 2 == 0)
                {
                    if(!jugadores[tir.dado2-1].isEmpty())
                    {
                        num = jugadores[tir.dado2-1].poll();
                        mesa.push(num);
                    }
                }
                else
                {
                    if(!mesa.isEmpty())
                    {
                        num = mesa.pop();
                        jugadores[tir.dado2-1].add(num);
                    }
                }
            }
            pos++;
        }

        this.print();

        // buscar el jugador con más fichas negras
        int jMax = 0;
        pos = 1;
        int fichas_max = 0;
        int fichas = 0;
        while(pos < jugadores.length)
        {
            fichas = 0;
            while(!jugadores[pos].isEmpty())
            {
                num = jugadores[pos].poll();

                if(num == 0)
                {
                    fichas++;
                }
            }
            if(fichas > fichas_max)
            {
                fichas_max = fichas;
                jMax = pos;
            }
            pos++;
        }
        // COMPLETAR


        return jMax;
    }

    private void print() {
        for (int i = 0; i < jugadores.length; i++) {
            String s = "<";
            while (!jugadores[i].isEmpty())
                s = s + " " + jugadores[i].poll().toString();
            s = s + ">";
            System.out.println(i + ": " + s);
        }
        String s = "<";
        while (!mesa.isEmpty())
            s = s + " " + mesa.pop().toString();
        s = s + ">";
        System.out.println("Mesa: " + s);
    }

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        ArrayList<Tirada> a = new ArrayList<Tirada>();
        a.add(new Tirada(2, 3));
        a.add(new Tirada(4, 1));
        a.add(new Tirada(3, 5));
        a.add(new Tirada(6, 3));

        new Juego().juego(5, a);

    }

}

