"""
This module contains DriveAmplifier Device Class and run method for it
"""

# Imports
from facadedevice import Facade, proxy_attribute, proxy_command, state_attribute
from tango import DevState, AttrWriteType, DispLevel


class DriveAmplifier(Facade):
    """
    DriveAmplifier Tango Device server exposes the state, attributes and
    command of the drive amplifier. All components are aggregated from the PLC
    device server. Writing and reading to and from DriveAmplifier device
    attributes is forwarded to reading and writing to and from the
    corresponding PLC signals. Executing commands of the DriveAmplifier Tango
    device is forwarded to writing to corresponding PLC signals. The state of
    the device is dictated by a set of PLC signals.
    """

    def safe_init_device(self):
        """
        This is method overriden from Facade base class. It is used to safely
        initialize DriveAmplifier device.
        """
        super(DriveAmplifier, self).safe_init_device()
        self.set_state(DevState.ON)
        self.set_status("Amplifier is running")

    # proxy attributes

    Temperature_Alarm = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ,
        display_level=DispLevel.OPERATOR,
        property_name="PLCAttName_TempA",
        description="Name of the PLC device attribute, corresponding to the "
                    "temperature alarm of the amplifier.")

    VSWR_Alarm = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ,
        display_level=DispLevel.OPERATOR,
        property_name="PLCAttName_VSWRA",
        description="Name of the PLC device attribute, corresponding to the "
                    "Voltage Standing Wave Ratio alarm of the amplifier.")

    PSU_Status = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ,
        display_level=DispLevel.OPERATOR,
        property_name="PLCAttName_PSUS",
        description="Name of the PLC device attribute, corresponding to the "
                    "Power Supply Unit status of the amplifier.")

    Interlock = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ,
        display_level=DispLevel.OPERATOR,
        property_name="PLCAttName_Interlock",
        description="Name of the PLC device attribute, corresponding to the "
                    "safety interlock of the amplifier.")

    Power = proxy_attribute(
        dtype=float,
        access=AttrWriteType.READ,
        display_level=DispLevel.OPERATOR,
        property_name="PLCAttName_Power",
        description="Name of the PLC device attribute, corresponding to the "
                    "forwarded power of the amplifier.")

    AmplifierState = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ,
        display_level=DispLevel.OPERATOR,
        property_name="PLCAttName_State",
        description="Name of the PLC device attribute, corresponding to the "
                    "forwarded power of the amplifier.")

    Bypass = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ_WRITE,
        display_level=DispLevel.OPERATOR,
        property_name="PLCAttName_Bypass",
        description="Name of the PLC device attribute, corresponding to the "
                    "bypass command of the amplifier.")

    # state attributes

    @state_attribute(
        bind=['Temperature_Alarm', 'VSWR_Alarm', 'PSU_Status', 'Interlock',
              'AmplifierState'])
    def check_alarms(self, temp, vswr, psu, inter, amplstate):
        """
        This attribute checks if any of the device alarms is on. If so,
        appropriate state and status are set for the device.

        :param temp: Temeprature_Alarm
        :param vswr: VSWR_Alarm
        :param psu: PSU_Status
        :param inter: Interlock
        :param amplstate: AmplifierState
        :return: ALARM, if any or the alarms is set
        :rtype: DevState
        """
        if temp or vswr or psu or inter or amplstate:
            return DevState.ALARM, "One or more alarms of the amplifier are active."

    # proxy commands

    @proxy_command(
        dtype_out=bool,
        write_attribute=True,
        property_name="PLCAttName_EnableTTL",
        doc_out="True to PLCAttName_EnableTTL")
    def EnableTtl(self, subcommand):
        """
        :rtype: bool
        """
        subcommand(1)
        return True

    @proxy_command(
        dtype_out=bool,
        write_attribute=True,
        property_name="PLCAttName_DisableTTL",
        doc_out="True to PLCAttName_DisableTTL")
    def DisableTtl(self, subcommand):
        """
        :rtype: bool
        """
        subcommand(1)
        return True

# run server

run = DriveAmplifier.run_server()

if __name__ == '__main__':
    run()
