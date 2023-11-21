try:
    from .starter import Starter
    from .state import go_next_state
except ImportError:
    from starter import Starter
    from state import go_next_state

def run():

    robot = Starter()

    while True:

        robot.on_entry()

        if robot.status == True:

            robot.execute()

            if robot.status == True:

                # Se NÂO HOUVER exceções "on_exit" define o "next_state"
                robot.on_exit()
                # Método da super classe para atualizar a instância
                robot = go_next_state(robot.next_state)

            elif robot.status == False:

                # Se HOUVER exceções "on_error" define o "next_state"
                robot.on_error()
                # Método da super classe para atualizar a instância
                robot = go_next_state(robot.next_state)

        elif robot.status == False:

            # Se HOUVER exceções "on_error" define o "next_state"
            robot.on_error()
            # Método da super classe para atualizar a instância
            robot = go_next_state(robot.next_state)

if __name__ == "__main__":
    run()