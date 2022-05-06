public class Campeonato {
    private Nodo root;

    public String campeon()
    {
        String champ = campeon(root);

        root.info.ganador = champ;
        return champ;
    }

    private String campeon(Nodo act)
    {
        if(act.info.golesDer != -1)
        {
            String champ_der = campeon(act.der);
            String champ_izq = campeon(act.izq);

            if(act.info.golesDer > act.info.golesIzq)
            {
                return champ_der;
            }
            else
            {
                return champ_izq;
            }
        }

        else
        {
            // Estoy en una hoja
            return act.info.ganador;

        }

    }
}
