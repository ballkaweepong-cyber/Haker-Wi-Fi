#!/usr/bin/env python3
import sys
import time
import os

os.system("clear")

ART = r"""
                      SySySSyyyySyyyyMySSSySy
yySySSySSSyyySSyySSSSSSySSSSSySSSySSyySySSyyySSSSySSSSSSyS.SySSySSSSSSyS.yyyyySyySyy.
yySSSSSyySSyyyyySSySSSSSSySSSySySySySySSSSSyySyySySySySSSy.yyyyySSyyyyySyyyyyySyyyyy.
ySM                                                                                 yS
ySS   yySySySyyySySSSSSySySSySSSSSySSSySSSSSSSySyySSSySyySyyyyyyyyyyyyyySyyyyyyyy   yS
ySM   SySSSSSSySSySSSSSSSyySySSSSSSSSSSSySSSSSSSSSSySSSSySyySSyyyyyyyyyyyyyyyyyyy   yS
ySM   SSSSSSSSSSSSSSSSSSSyMMM                             MMSSyySSSSySSSSyyySSyyy   yS
SSS   SSSSSSSSSSSSSSMMMM                                       MMSySySSSSyyyyyyyy   yS
SMM   SSSSMSSSyMMMM                                                 MMMMSyyyySSyy   yS
SMM   SSSSMSSMM                                                         MMSSSSSSy   yM
SMM   SSSMMS                                                              yMMSSyy   yM
SMM   SSMy                                                                  ySMSS   yS
SMM   y                                                                        .y   yS
SMM                                                                                 SM
SMM   SS                                                                      .SS   SM
SSM   SSMSS           SSMSSMS.                           MySSSSMy           SSSSS   yM
SMM   SSSSMSS     MMSSSSSSSSyMSSSS                   SSSSSySSSSSSSSy      SSySSyy   SM
SMM   yyySMSS SSSSSSSSMySSSSSMSSSSSMS             MMSSSSSMSSMSSyySMSSSSS  SSSSyyy   yM
SMM   SSSSMSSSSSSyMMyySySSyMySSSSSSSSSSSyS   SySSSSSMSSSSSSMMSSyyyMMMyySS SSySSSS   yM
SSM   .yyyMSS.MMyy.          yMySSSMSSSMMMS SSMMSSSSMSyMMy.         .y.MM SySyyyy   yS
SMM   SSSySSM                  .yMMMSSSSyMy MMSSSSSyMy..                  MyyySyy   yM
SMM   MMMMS.    .M         ....   .yMMMM..   .yMMMM..    .          .M      MSMSS   yM
SMM   y..     SSM     .SSSMMSMSSSSyy               yySSSMMMSSSSS.    yMS      .y.   yS
SMM           SSM    SSSSySSySSSSSSMy   yS   yS   MSSSSSSSSySSSSSy   .SS            SM
SMM           SM.    SSMMSSMSSMSSMSMM   MS   MS   MSSSSSSSSMMSSMSy     M            yM
SMM             M  SSMMMMSMMSMSSSMMM   .SM   SM.   MSMSSSSyMMMSMMySS  M             yS
SMM               SSMMy     MMMSMSS    S      yS    ySMMSSM     MMSSy               yM
SSM                                   yS.      SS                                   yS
SMM           yyS                  SyS           SS.                 ySy            yM
SMM         ySSSS                 SS               MM                .ySSyS         yM
SMM       MSSSSS                  SS               SM                  SSSSSy       yM
SMM      MMSSSSSM             MMMSMMMSM         MMMSMMMSS             MSSySSMy      yM
SSM     MSMSSSSSSM        MMSMMSSSSMSSSMM.   yMMSSSSMSSSSMMMS       .MSSSySSSSM     yS
SMM     SSMSSSSSSSMMMMMMMMSSSMSSSSSMSSSSSMMMMMSSSSSSMSSSSMSSSMMMMMSMSSSSSySSySS     yM
SMM     MSMSSSSSSSSSSSSSSSSSSMMSSSSMSSSSSMMSMSSSSSSSMSSSSMSSSSSSSSSSSSSSSSySSSS     yM
SSM   y  MMSSSSSSSSSSSSSSSSSSMSSSSSMSSSSSMSSSSSSSSSSSSSSSSSSSSSSSySSSSSSSSySSy yy   yM
SMM   SSSyMSSSSSSSSSSSSSSSSSySSSSSSSSSSSSSSSSSSSSSSSSSSSSSSySSSSSySySSSSSyySyyySy   yM
SMM   SSSS.SySSSSSSSSSMSSSSSSMSSS     SSSMSMSSSSS     SSSMSSSSSSSySSSSSSMSS.ySSSy   yS
SMM   SSSSMM.yyMMMMMSSSSS       yMMMMS           SMMSSy        MSSSyMMMMyy ySSSyy   yM
SMM   SSSSMSS              MSMSSSSSSSSSSyMSSyMMSSSSSMSSSSSyM              SSSSSSy   yM
SMM   SSSSMSSM               MMSSSSMSSSSSMSSSSSSSSSSSSSSyM               SSSSSSSy   yM
SMM   SSSSMSSSy                MMSSSSySSSSSSSSSSSSSyMMM.                yySyySyyy   yS
SMM   SSSSMSSSy                  yySMyyMyMMMyMMMSSMySS                  SSSSSSSSy   yM
SMM   SSSSMSSSy.                     yyyySyyySSyyS                     .SySSySSSS   yM
SMM   SSSSMSSSSS                                                       SSySSSSSSy   SM
SMM   SSSSMSSSSSS                                                    .SSSSSSySSSS   yS
ySS   SySSMSSSySMy                                                  yyMSSySyySyyy   yS
SMM   SSSSMSSSSSSSSM.                                             ySSSSSSSSSySSSy   yS
SMM   SSSSMSSSSSSSSSSS.                                         .SSSSSSSSSSSySSSy   SM
SSM   SSSSMSSSSSSSMSSMMSy                                     ySSSSSSSSSSSSSySSSy   yM
SMM   SSSSSSSSSSSSSSSSSSSS                                   SSSSSSSSSSSSyySySSyy   SM
SMM   SSSSMMSSSSMSSSSMSSSySMS            SSSMy           ySSSSSSSSSSSSSSSSySSSSSS   yM
SSM   SSSSMSSSSSSSSSSSSSSSSSMSy         SMMMMMS         yMSySSSSyySSSSySSyySySyyy   yM
SMM...... ....... ....... ....... ........... ...... . .. ..  ... ..  ... .    .. . yM
"""

print(ART)
print()

# Progress bar like the screenshot
width = 42
for percent in range(101):
    filled = int(width * percent / 100)
    bar = "█" * filled + " " * (width - filled)
    sys.stdout.write(f"\r|{bar}| {percent}%")
    sys.stdout.flush()
    time.sleep(0.018)

print("\n")
print(">>> READY")
