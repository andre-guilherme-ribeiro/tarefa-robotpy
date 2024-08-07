import wpilib
import wpilib.drive
import phoenix5
import rev

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.left_front = phoenix5.WPI_TalonSRX(1)

        self.left_back = rev.CANSparkMax(2, rev.CANSparkLowLevel.MotorType.kBrushless)

        self.right_front = rev.CANSparkMax(3, rev.CANSparkLowLevel.MotorType.kBrushless)

        self.right_back = phoenix5.WPI_TalonSRX(4)
        
        self.left = wpilib.MotorControllerGroup(self.left_front, self.left_back)

        self.right = wpilib.MotorControllerGroup(self.right_front, self.right_back)

        self.right.setInverted(True)

      
        self.drivetrain = wpilib.drive.DifferentialDrive(self.left, self.right)
        
        self.joystick = wpilib.Joystick(0)

        self.elevacao = phoenix5.WPI_VictorSPX(5)

    def teleopPeriodic(self):
        self.drivetrain.arcadeDrive(-self.joystick.getRawAxis(1), self.joystick.getRawAxis(0))

        if self.joystick.getRawButton(5):
            self.elevacao.set(0.5)
        else:
            self.elevacao.set(0.0)
