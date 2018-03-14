import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import static java.lang.StrictMath.sqrt;


/**
 * Created by nathanjekel on 3/23/17.
 */
public class Calculator extends JFrame implements ActionListener{

    private JMenuBar menu_bar;
    private JMenu file_menu, help_menu;
    private JMenuItem exit_menu_item;
    private JTextField screen;
    private JButton calc_buttons[];
    private JPanel calculator, backspace, clear, buttons;
    private Double a = 0.0, b = 0.0, result = 0.0;
    private Integer operator = 0;
    private Integer firstOperandLength = 0;

    public Calculator () {

        super("Calculator");

        //
        // Create Menu Bar
        file_menu = new JMenu("File");
        exit_menu_item = new JMenuItem("Exit");
        file_menu.add(exit_menu_item);
        help_menu = new JMenu("Help");
        menu_bar = new JMenuBar();
        menu_bar.add(file_menu);
        menu_bar.add(help_menu);
        setJMenuBar(menu_bar);

        //
        // Create Overall Border Layout
        calculator = new JPanel();
        screen = new JTextField("");
        screen.setEditable(false);
        getContentPane().add(screen, BorderLayout.NORTH);
        calc_buttons = new JButton[23];

        //
        // Create calculator panels
        buttons = new JPanel();
        backspace = new JPanel();
        clear = new JPanel();

        //
        // Create calculator buttons
        for (int i = 0; i <= 9; i++) {
            calc_buttons[i] = new JButton(String.valueOf(i));
        }

        calc_buttons[10] = new JButton("+/-");
        calc_buttons[11] = new JButton(".");
        calc_buttons[12] = new JButton("=");
        calc_buttons[13] = new JButton("/");
        calc_buttons[14] = new JButton("*");
        calc_buttons[15] = new JButton("-");
        calc_buttons[16] = new JButton("+");
        calc_buttons[17] = new JButton("sqrt");
        calc_buttons[18] = new JButton("1/x");
        calc_buttons[19] = new JButton("%");
        calc_buttons[20] = new JButton("Backspace");
        calc_buttons[21] = new JButton(" CE ");
        calc_buttons[22] = new JButton("C");

        // Set appropriate button colors
        for (int i = 0; i < calc_buttons.length; i++) {
            if (i < 10) { calc_buttons[i].setForeground(Color.blue); }
			else { calc_buttons[i].setForeground(Color.red); }
        }

        //
        // Create layouts for panels and add buttons
        backspace.setLayout(new GridLayout(1, 1, 2, 2));
        backspace.add(calc_buttons[20]);
        clear.setLayout(new GridLayout(1, 2, 2, 2));
        clear.add(calc_buttons[21]);
        clear.add(calc_buttons[22]);
        buttons.setLayout(new GridLayout(4,5, 2, 2 ));

        // Add buttons to in appropriate order
        buttons.add(calc_buttons[7]);
        buttons.add(calc_buttons[8]);
        buttons.add(calc_buttons[9]);
        buttons.add(calc_buttons[13]);
        buttons.add(calc_buttons[17]);
        buttons.add(calc_buttons[4]);
        buttons.add(calc_buttons[5]);
        buttons.add(calc_buttons[6]);
        buttons.add(calc_buttons[14]);
        buttons.add(calc_buttons[18]);
        buttons.add(calc_buttons[1]);
        buttons.add(calc_buttons[2]);
        buttons.add(calc_buttons[3]);
        buttons.add(calc_buttons[15]);
        buttons.add(calc_buttons[19]);
        buttons.add(calc_buttons[0]);
        buttons.add(calc_buttons[10]);
        buttons.add(calc_buttons[11]);
        buttons.add(calc_buttons[16]);
        buttons.add(calc_buttons[12]);

        //
        // Set button size
        for (int i = 0; i < 20; i++) {
            calc_buttons[i].setPreferredSize(new Dimension(60, 60));
        }

        //
        // Add panels to calculator panel
        calculator.setLayout(new BorderLayout());
        calculator.add(backspace, BorderLayout.WEST);
        calculator.add(clear, BorderLayout.EAST);
        calculator.add(buttons, BorderLayout.SOUTH);

        //
        // Add Calculator Panel to JFrame
        getContentPane().add(calculator, BorderLayout.SOUTH);

        //
        // Set up Action Listener for all buttons
        exit_menu_item.addActionListener(this);
        for (int i = 0; i < calc_buttons.length; i++) {
            calc_buttons[i].addActionListener(this);
        }

        //
        // Set Application Specifications
        setSize(400, 400);
        setLocationRelativeTo(null);
        setResizable(false);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }


    @Override
    public void actionPerformed(ActionEvent actionEvent) {

        if(actionEvent.getSource() == calc_buttons[0])
            screen.setText(screen.getText().concat("0"));

        else if(actionEvent.getSource() == calc_buttons[1])
            screen.setText(screen.getText().concat("1"));

        else if(actionEvent.getSource() == calc_buttons[2])
            screen.setText(screen.getText().concat("2"));

        else if(actionEvent.getSource() == calc_buttons[3])
            screen.setText(screen.getText().concat("3"));

        else if(actionEvent.getSource() == calc_buttons[4])
            screen.setText(screen.getText().concat("4"));

        else if(actionEvent.getSource() == calc_buttons[5])
            screen.setText(screen.getText().concat("5"));

        else if(actionEvent.getSource() == calc_buttons[6])
            screen.setText(screen.getText().concat("6"));

        else if(actionEvent.getSource() == calc_buttons[7])
            screen.setText(screen.getText().concat("7"));

        else if(actionEvent.getSource() == calc_buttons[8])
            screen.setText(screen.getText().concat("8"));

        else if(actionEvent.getSource() == calc_buttons[9])
            screen.setText(screen.getText().concat("9"));

        else if(actionEvent.getSource() == calc_buttons[11])
            screen.setText(screen.getText().concat("."));

        else if(actionEvent.getSource() == calc_buttons[10]) {
            a = Double.parseDouble(screen.getText());
            result = a * -1;
            screen.setText(String.valueOf(result));
        }

        else if(actionEvent.getSource() == calc_buttons[13])
        {
            a=Double.parseDouble(screen.getText());
            operator = 1;
            screen.setText(screen.getText().concat("/"));
            firstOperandLength = screen.getText().length();

        }

        else if(actionEvent.getSource() == calc_buttons[14])
        {
            a=Double.parseDouble(screen.getText());
            operator = 2;
            screen.setText(screen.getText().concat("*"));
            firstOperandLength = screen.getText().length();

        }

        else if(actionEvent.getSource() == calc_buttons[15])
        {
            a=Double.parseDouble(screen.getText());
            operator = 3;
            screen.setText(screen.getText().concat("-"));
            firstOperandLength = screen.getText().length();

        }

        else if(actionEvent.getSource() == calc_buttons[16])
        {
            a=Double.parseDouble(screen.getText());
            operator = 4;
            screen.setText(screen.getText().concat("+"));
            firstOperandLength = screen.getText().length();

        }

        else if(actionEvent.getSource() == calc_buttons[17])
        {
            operator = 5;
            screen.setText("sqrt(");
            firstOperandLength = screen.getText().length();

        }

        else if(actionEvent.getSource() == calc_buttons[18])
        {
            operator = 6;
            screen.setText("1/");
            firstOperandLength = screen.getText().length();

        }

        else if(actionEvent.getSource() == calc_buttons[19])
        {
            a = Double.parseDouble(screen.getText());
            operator = 7;
            screen.setText(screen.getText().concat("%"));
            firstOperandLength = screen.getText().length();
        }

        else if(actionEvent.getSource() == calc_buttons[12]) {
            Integer expressionLength = screen.getText().length();
            b = Double.parseDouble(screen.getText().substring(firstOperandLength, expressionLength));
            switch(operator)
            {
                case 1: result=a/b;
                    break;

                case 2: result=a*b;
                    break;

                case 3: result=a-b;
                    break;

                case 4: result=a+b;
                    break;
                case 5: result = sqrt(b);
                    break;
                case 6: result = 1.0/b;
                    break;
                case 7: result = a%b;
                    break;
                default: result = 0.0;
            }

            screen.setText(""+result);
        }

        else if(actionEvent.getSource() == calc_buttons[20])
        {
            String s=screen.getText();
            screen.setText("");
            for(int i=0;i<s.length()-1;i++)
                screen.setText(screen.getText()+s.charAt(i));
        }

        else screen.setText("");


    }


    public static void main(String[] args) {

        new Calculator();

    }

}


