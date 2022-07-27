#!/usr/bin/env python
# -*- coding: utf-8 -*-

import qi
import argparse
import sys


def main(session):

    ad = session.service("ALAudioDevice")
    tts = session.service("ALTextToSpeech")

    # modify volume value to change volume
    volume = 40
    ad.setOutputVolume(volume)
    tts.setLanguage("Japanese")
    # Say Emile in english
    tts.say("聞こえますか？")

    print(ad.getOutputVolume())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
    
    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
