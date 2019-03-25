# Importing Common Language Runtime Module in addition to powershell relevant modules
import clr
import sys 
import System
clr.AddReference("System.Management.Automation")
clr.AddReference("Microsoft.Build.Engine")
clr.AddReference("System.Management")
from Microsoft.Build.BuildEngine import *
from System.Management.Automation import RunspaceInvoke, PSMethod
from System.Management import ManagementObjectSearcher
from System.Management import ConnectionOptions, ManagementScope
# --------------------------------------------------------------------------------------------
# Defining M@gic Menu
def MagicMenu():
    print (" -------- M@gic Menu -------- ")
    print()

    choice = input("""
                      1. Run Powershell commands without spawning powershell.exe - .NET Runspace
                      2. Run MSBUILD during runtime and compile in runtime + in memory
                      3. Query the system for drives info using a WMI query
                      4. Connect to a remote computer using WMI
                      9. Perform Enumeration to the system to find possible Privilege Escalation possibilities 
                      10. Quit
    
                        Please Enter Your Choice: """)
    if choice == 1:
        pshmenu()
    elif choice == 2:
        MSMagic()
    elif choice == 3:
        sysq()
    elif choice == 4:
        WMIQ()
    elif choice == 5:
        WMIOPS()
    elif choice == 9:
        Priv()
    elif choice == 10:
        sys.exit
    else:
        print("You Didn't select an option.")
        print("Please try again")
        MagicMenu()
# --------------------------------------------------------------------------------------------
# Define PSH Menu
def pshmenu():
    print (" --- PSH Menu --- ")
    choice = input("""
                      1. Run Powershell Commands
                      2. Get a reverse shell using native powershell socket
                      3. Return to M@gic Menu
 
                       Please Enter Your Choice: """)
    if choice == 1:
     inpcmd = raw_input("Please Enter a command to execute: ")
     pshrunspace(inpcmd)
    elif choice == 2:
     print ("Will get updated later")
    elif choice == 3:
     MagicMenu()
    else:
     print("Something went wrong, Please try again")
     pshmenu()
# --------------------------------------------------------------------------------------------
# Defining Privilege Escalation Function

# --------------------------------------------------------------------------------------------
# Defining PSH function
def pshrunspace (commandex):
 runspace = RunspaceInvoke()
 cmd = runspace.Invoke(commandex) #Execute Commands
 process = (cmd)
 for x in cmd:
     print x
# --------------------------------------------------------------------------------------------
# Define MBSUILD Function
def MSMagic():
    projpath = raw_input("Please enter the project location: ")
    e = Engine()
    e.BinPath = System.Runtime.InteropServices.RuntimeEnvironment.GetRuntimeDirectory()
    log = ConsoleLogger()
    e.RegisterLogger(log)
    e.BuildProjectFile(projpath)
# --------------------------------------------------------------------------------------------
# Define query system function 
def sysq():
    query = "Select * from Win32_LogicalDisk"
    searcher = ManagementObjectSearcher(query)
    for drive in searcher.Get():
        for p in drive.Properties:
            print p.Name, p.Value
        print
# --------------------------------------------------------------------------------------------
# Define remote connection using WMI
def WMIQ():
    options = ConnectionOptions()
    options.EnablePrivileges = True
    cmpname = raw_input("Please enter the remote computer name: ")
    options.Username = raw_input("Please enter the username: ")
    options.Password = raw_input("Please enter the password: ")
    network_scope = r"\\cmpname\root\cimv2"
    scope = ManagementScope(network_scope, options)
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# Privilege Escalation Function
def Priv():
    print("M@gic Privilege Escalation - Beware this is bl@ck magic ...")
    def RunAll():
        print("Checking Always Install Elevated")
        AIE()
# -------------
    def AIE():
        print(" --- Always Install Elevated Check --- ")
        inpcmd = str("reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated ('&') reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated")
        res = pshrunspace(inpcmd)
        if res is None:
            print("No results returned")
# -------------
    def PWCheck():
        print("Checking credentials in the system in various common places")
        inpcmd = ('')
        res = pshrunspace(inpcmd)
        if res is None:
            print("No results returned")
# -------------
    def WinV():
        winver = System.Environment.OSVersion
        print winver
        Priv()

    choice = input("""
                      1. Run All Checks ( May produce a bit noise in the system )
                      2. Search for - AlwaysInstallElavated -
                      3. Find stored credentials
                      10. Return to M@gic Main Menu
    
                        Please Pick a choice: """)
    if choice == 1:
        RunAll()
    elif choice == 2:
        AIE()
    elif choice == 3:
        PWCheck()
    elif choice == 4:
        WinV()
    elif choice == 10:
        MagicMenu()
    else:
        print("You didn't pick a choice, Please pick a choice: ")
        Priv()
print ('-----------------------------------------------------------------------------')
print('              M@gic - A tool that simply performs black magic')
print ('Author: SysBuf3r - Hack till you reach the system buffer then overflow it :)')
print ('-----------------------------------------------------------------------------')
MagicMenu()