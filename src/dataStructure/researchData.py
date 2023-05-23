import os
import pandas as pd

absolute_path = os.path.abspath(os.path.dirname("data.csv"))

emo_ann_external = pd.read_csv(
    "dataset/emotion_annotations/aggregated_external_annotations/P4.external.csv"
)
emo_ann_partner = pd.read_csv(
    "dataset/emotion_annotations/partner_annotations/P4.partner.csv"
)
emo_ann_self = pd.read_csv("dataset/emotion_annotations/self_annotations/P4.self.csv")

E4_ACC = pd.read_csv("dataset/e4_data/4/E4_ACC.csv")
E4_BVP = pd.read_csv("dataset/e4_data/4/E4_BVP.csv")
E4_EDA = pd.read_csv("dataset/e4_data/4/E4_EDA.csv")
E4_HR = pd.read_csv("dataset/e4_data/4/E4_HR.csv")
E4_IBI = pd.read_csv("dataset/e4_data/4/E4_IBI.csv")
E4_TEMP = pd.read_csv("dataset/e4_data/4/E4_TEMP.csv")

Attention = pd.read_csv("dataset/neurosky_polar_data/4/Attention.csv")
BrainWave = pd.read_csv("dataset/neurosky_polar_data/4/BrainWave.csv")
Meditation = pd.read_csv("dataset/neurosky_polar_data/4/Meditation.csv")
Polar_HR = pd.read_csv("dataset/neurosky_polar_data/4/Polar_HR.csv")

import random
from component.viewGraphComponent import ViewGraphComponent
from models.graphDataModel import GraphPlotDataModel, GraphTraceDataModel


class ResearchDataFactory:
    def __random_timeseries(
        self,
        initial_value: float,
        volatility: float,
        count: int,
    ) -> list:
        time_series = [
            initial_value,
        ]
        for _ in range(count):
            time_series.append(
                time_series[-1] + initial_value * random.gauss(0, 1) * volatility
            )
        return time_series

    def __init__(self):
        data_x = list(E4_ACC["x"])
        data_y = list(E4_ACC["y"])
        data_z = list(E4_ACC["z"])
        data_bvp = list(E4_BVP["value"])
        data_eda = list(E4_EDA["value"])
        data_hr_e4 = list(E4_HR["value"])
        data_ibi = list(E4_IBI["value"])
        data_temp = list(E4_TEMP["value"])
        data_brainwave_delta = list(BrainWave["delta"])
        data_brainwave_theta = list(BrainWave["theta"])
        data_brainwave_low_alpha = list(BrainWave["lowAlpha"])
        data_brainwave_high_alpha = list(BrainWave["highAlpha"])
        data_brainwave_low_beta = list(BrainWave["lowBeta"])
        data_brainwave_high_beta = list(BrainWave["highBeta"])
        data_brainwave_low_gamma = list(BrainWave["lowGamma"])
        data_brainwave_middle_gamma = list(BrainWave["middleGamma"])
        data_att = list(Attention["value"])
        data_med = list(Meditation["value"])
        data_hr_ecg = list(Polar_HR["value"])

        data_ext_arousal = list(emo_ann_external["arousal"])
        data_ext_valence = list(emo_ann_external["valence"])
        data_ext_stress_cheerful = list(emo_ann_external["cheerful"])
        data_ext_stress_happy = list(emo_ann_external["happy"])
        data_ext_stress_angry = list(emo_ann_external["angry"])
        data_ext_stress_nervous = list(emo_ann_external["nervous"])
        data_ext_stress_sad = list(emo_ann_external["sad"])
        data_ext_cBROMP_boredom = list(emo_ann_external["boredom"])
        data_ext_cBROMP_confusion = list(emo_ann_external["confusion"])
        data_ext_cBROMP_delight = list(emo_ann_external["delight"])
        data_ext_cBROMP_concentration = list(emo_ann_external["concentration"])
        data_ext_cBROMP_frustration = list(emo_ann_external["frustration"])
        data_ext_cBROMP_surprise = list(emo_ann_external["surprise"])
        data_ext_cBROMP_none_1 = list(emo_ann_external["none_1"])
        data_ext_lcBROMP_confrustion = list(emo_ann_external["confrustion"])
        data_ext_lcBROMP_contempt = list(emo_ann_external["contempt"])
        data_ext_lcBROMP_dejection = list(emo_ann_external["dejection"])
        data_ext_lcBROMP_disgust = list(emo_ann_external["disgust"])
        data_ext_lcBROMP_eureka = list(emo_ann_external["eureka"])
        data_ext_lcBROMP_pride = list(emo_ann_external["pride"])
        data_ext_lcBROMP_sorrow = list(emo_ann_external["sorrow"])
        data_ext_lcBROMP_none_2 = list(emo_ann_external["none_2"])

        data_pnr_arousal = list(emo_ann_partner["arousal"])
        data_pnr_valence = list(emo_ann_partner["valence"])
        data_pnr_stress_cheerful = list(emo_ann_partner["cheerful"])
        data_pnr_stress_happy = list(emo_ann_partner["happy"])
        data_pnr_stress_angry = list(emo_ann_partner["angry"])
        data_pnr_stress_nervous = list(emo_ann_partner["nervous"])
        data_pnr_stress_sad = list(emo_ann_partner["sad"])
        data_pnr_cBROMP_boredom = list(emo_ann_partner["boredom"])
        data_pnr_cBROMP_confusion = list(emo_ann_partner["confusion"])
        data_pnr_cBROMP_delight = list(emo_ann_partner["delight"])
        data_pnr_cBROMP_concentration = list(emo_ann_partner["concentration"])
        data_pnr_cBROMP_frustration = list(emo_ann_partner["frustration"])
        data_pnr_cBROMP_surprise = list(emo_ann_partner["surprise"])
        data_pnr_cBROMP_none_1 = list(emo_ann_partner["none_1"])
        data_pnr_lcBROMP_confrustion = list(emo_ann_partner["confrustion"])
        data_pnr_lcBROMP_contempt = list(emo_ann_partner["contempt"])
        data_pnr_lcBROMP_dejection = list(emo_ann_partner["dejection"])
        data_pnr_lcBROMP_disgust = list(emo_ann_partner["disgust"])
        data_pnr_lcBROMP_eureka = list(emo_ann_partner["eureka"])
        data_pnr_lcBROMP_pride = list(emo_ann_partner["pride"])
        data_pnr_lcBROMP_sorrow = list(emo_ann_partner["sorrow"])
        data_pnr_lcBROMP_none_2 = list(emo_ann_partner["none_2"])

        data_self_arousal = list(emo_ann_self["arousal"])
        data_self_valence = list(emo_ann_self["valence"])
        data_self_stress_cheerful = list(emo_ann_self["cheerful"])
        data_self_stress_happy = list(emo_ann_self["happy"])
        data_self_stress_angry = list(emo_ann_self["angry"])
        data_self_stress_nervous = list(emo_ann_self["nervous"])
        data_self_stress_sad = list(emo_ann_self["sad"])
        data_self_cBROMP_boredom = list(emo_ann_self["boredom"])
        data_self_cBROMP_confusion = list(emo_ann_self["confusion"])
        data_self_cBROMP_delight = list(emo_ann_self["delight"])
        data_self_cBROMP_concentration = list(emo_ann_self["concentration"])
        data_self_cBROMP_frustration = list(emo_ann_self["frustration"])
        data_self_cBROMP_surprise = list(emo_ann_self["surprise"])
        data_self_cBROMP_none_1 = list(emo_ann_self["none_1"])
        data_self_lcBROMP_confrustion = list(emo_ann_self["confrustion"])
        data_self_lcBROMP_contempt = list(emo_ann_self["contempt"])
        data_self_lcBROMP_dejection = list(emo_ann_self["dejection"])
        data_self_lcBROMP_disgust = list(emo_ann_self["disgust"])
        data_self_lcBROMP_eureka = list(emo_ann_self["eureka"])
        data_self_lcBROMP_pride = list(emo_ann_self["pride"])
        data_self_lcBROMP_sorrow = list(emo_ann_self["sorrow"])
        data_self_lcBROMP_none_2 = list(emo_ann_self["none_2"])

        # data_audio = self.__random_timeseries(0.01, 4, 600)

        ########### create line plot with the data ##################

        traceData_acc_x = GraphTraceDataModel("x axis", data_x)
        traceData_acc_y = GraphTraceDataModel("y axis", data_y)
        traceData_acc_z = GraphTraceDataModel("z axis", data_z)
        self.plotData_acc = GraphPlotDataModel(
            "g",
            [
                traceData_acc_x,
                traceData_acc_y,
                traceData_acc_z,
            ],
        )

        traceData_bvp = GraphTraceDataModel("BVP", data_bvp)
        self.plotData_bvp = GraphPlotDataModel("PPG", [traceData_bvp])

        traceData_eda = GraphTraceDataModel("EDA", data_eda)
        self.plotData_eda = GraphPlotDataModel("uS", [traceData_eda])

        traceData_hr_e4 = GraphTraceDataModel("E4", data_hr_e4)
        traceData_hr_ecg = GraphTraceDataModel("ECG", data_hr_ecg)
        self.plotData_hr = GraphPlotDataModel(
            "Heart Rate", [traceData_hr_e4, traceData_hr_ecg]
        )

        traceData_ibi = GraphTraceDataModel("IBI", data_ibi)
        self.plotData_ibi = GraphPlotDataModel("IBI", [traceData_ibi])

        traceData_temp = GraphTraceDataModel("℃", data_temp)
        self.plotData_temp = GraphPlotDataModel("Temperature", [traceData_temp])

        traceData_bw_high_alpha = GraphTraceDataModel(
            "high-alpha", data_brainwave_high_alpha
        )
        traceData_bw_high_beta = GraphTraceDataModel(
            "high-beta", data_brainwave_high_beta
        )
        traceData_bw_middle_gamma = GraphTraceDataModel(
            "middle-gamma", data_brainwave_middle_gamma
        )
        traceData_bw_low_alpha = GraphTraceDataModel(
            "low-alpha", data_brainwave_low_alpha
        )
        traceData_bw_low_beta = GraphTraceDataModel("low-beta", data_brainwave_low_beta)
        traceData_bw_low_gamma = GraphTraceDataModel(
            "low-gamma", data_brainwave_low_gamma
        )
        traceData_bw_delta = GraphTraceDataModel("delta", data_brainwave_delta)
        traceData_bw_theta = GraphTraceDataModel("theta", data_brainwave_theta)
        self.plotData_bw = GraphPlotDataModel(
            "relative power",
            [
                traceData_bw_high_alpha,
                traceData_bw_high_beta,
                traceData_bw_middle_gamma,
                traceData_bw_low_alpha,
                traceData_bw_low_beta,
                traceData_bw_low_gamma,
                traceData_bw_delta,
                traceData_bw_theta,
            ],
        )

        traceData_att = GraphTraceDataModel("attention", data_att)
        traceData_med = GraphTraceDataModel("meditation", data_med)
        self.plotData_etc = GraphPlotDataModel(
            "attention & meditation", [traceData_att, traceData_med]
        )

        # traceData_audio = GraphTraceDataModel("audio", data_audio)
        # self.plotData_audio = GraphPlotDataModel("audio", [traceData_audio])

        traceData_ext_arousal = GraphTraceDataModel("arousal", data_ext_arousal)
        traceData_ext_valence = GraphTraceDataModel("valence", data_ext_valence)
        traceData_ext_cheerful = GraphTraceDataModel(
            "cheerful", data_ext_stress_cheerful
        )
        traceData_ext_happy = GraphTraceDataModel("happy", data_ext_stress_happy)
        traceData_ext_angry = GraphTraceDataModel("angry", data_ext_stress_angry)
        traceData_ext_nervous = GraphTraceDataModel("nervous", data_ext_stress_nervous)
        traceData_ext_sad = GraphTraceDataModel("sad", data_ext_stress_sad)
        traceData_ext_boredom = GraphTraceDataModel("boredom", data_ext_cBROMP_boredom)
        traceData_ext_confusion = GraphTraceDataModel(
            "confusion", data_ext_cBROMP_confusion
        )
        traceData_ext_delight = GraphTraceDataModel("delight", data_ext_cBROMP_delight)
        traceData_ext_concentration = GraphTraceDataModel(
            "concentration", data_ext_cBROMP_concentration
        )
        traceData_ext_frustration = GraphTraceDataModel(
            "frustration", data_ext_cBROMP_frustration
        )
        traceData_ext_surprise = GraphTraceDataModel(
            "surprise", data_ext_cBROMP_surprise
        )
        traceData_ext_none_1 = GraphTraceDataModel(
            "commonly used BROMP none", data_ext_cBROMP_none_1
        )
        traceData_ext_confrustion = GraphTraceDataModel(
            "confrustion", data_ext_lcBROMP_confrustion
        )
        traceData_ext_contempt = GraphTraceDataModel(
            "contempt", data_ext_lcBROMP_contempt
        )
        traceData_ext_dejection = GraphTraceDataModel(
            "dejection", data_ext_lcBROMP_dejection
        )
        traceData_ext_disgust = GraphTraceDataModel("disgust", data_ext_lcBROMP_disgust)
        traceData_ext_eureka = GraphTraceDataModel("eureka", data_ext_lcBROMP_eureka)
        traceData_ext_pride = GraphTraceDataModel("pride", data_ext_lcBROMP_pride)
        traceData_ext_sorrow = GraphTraceDataModel("sorrow", data_ext_lcBROMP_sorrow)
        traceData_ext_none_2 = GraphTraceDataModel(
            "less commonly used BROMP none", data_ext_lcBROMP_none_2
        )

        self.plotData_emo_ann_ext = GraphPlotDataModel(
            "external emotion annotation",
            [
                traceData_ext_arousal,
                traceData_ext_valence,
                traceData_ext_cheerful,
                traceData_ext_happy,
                traceData_ext_angry,
                traceData_ext_nervous,
                traceData_ext_sad,
                traceData_ext_boredom,
                traceData_ext_confusion,
                traceData_ext_delight,
                traceData_ext_concentration,
                traceData_ext_frustration,
                traceData_ext_surprise,
                traceData_ext_none_1,
                traceData_ext_confrustion,
                traceData_ext_contempt,
                traceData_ext_dejection,
                traceData_ext_disgust,
                traceData_ext_eureka,
                traceData_ext_pride,
                traceData_ext_sorrow,
                traceData_ext_none_2,
            ],
        )

        traceData_pnr_arousal = GraphTraceDataModel("arousal", data_pnr_arousal)
        traceData_pnr_valence = GraphTraceDataModel("valence", data_pnr_valence)
        traceData_pnr_cheerful = GraphTraceDataModel(
            "cheerful", data_pnr_stress_cheerful
        )
        traceData_pnr_happy = GraphTraceDataModel("happy", data_pnr_stress_happy)
        traceData_pnr_angry = GraphTraceDataModel("angry", data_pnr_stress_angry)
        traceData_pnr_nervous = GraphTraceDataModel("nervous", data_pnr_stress_nervous)
        traceData_pnr_sad = GraphTraceDataModel("sad", data_pnr_stress_sad)
        traceData_pnr_boredom = GraphTraceDataModel("boredom", data_pnr_cBROMP_boredom)
        traceData_pnr_confusion = GraphTraceDataModel(
            "confusion", data_pnr_cBROMP_confusion
        )
        traceData_pnr_delight = GraphTraceDataModel("delight", data_pnr_cBROMP_delight)
        traceData_pnr_concentration = GraphTraceDataModel(
            "concentration", data_pnr_cBROMP_concentration
        )
        traceData_pnr_frustration = GraphTraceDataModel(
            "frustration", data_pnr_cBROMP_frustration
        )
        traceData_pnr_surprise = GraphTraceDataModel(
            "surprise", data_pnr_cBROMP_surprise
        )
        traceData_pnr_none_1 = GraphTraceDataModel(
            "commonly used BROMP none", data_pnr_cBROMP_none_1
        )
        traceData_pnr_confrustion = GraphTraceDataModel(
            "confrustion", data_pnr_lcBROMP_confrustion
        )
        traceData_pnr_contempt = GraphTraceDataModel(
            "contempt", data_pnr_lcBROMP_contempt
        )
        traceData_pnr_dejection = GraphTraceDataModel(
            "dejection", data_pnr_lcBROMP_dejection
        )
        traceData_pnr_disgust = GraphTraceDataModel("disgust", data_pnr_lcBROMP_disgust)
        traceData_pnr_eureka = GraphTraceDataModel("eureka", data_pnr_lcBROMP_eureka)
        traceData_pnr_pride = GraphTraceDataModel("pride", data_pnr_lcBROMP_pride)
        traceData_pnr_sorrow = GraphTraceDataModel("sorrow", data_pnr_lcBROMP_sorrow)
        traceData_pnr_none_2 = GraphTraceDataModel(
            "less commonly used BROMP none", data_pnr_lcBROMP_none_2
        )

        self.plotData_emo_ann_pnr = GraphPlotDataModel(
            "partner emotion annotation",
            [
                traceData_pnr_arousal,
                traceData_pnr_valence,
                traceData_pnr_cheerful,
                traceData_pnr_happy,
                traceData_pnr_angry,
                traceData_pnr_nervous,
                traceData_pnr_sad,
                traceData_pnr_boredom,
                traceData_pnr_confusion,
                traceData_pnr_delight,
                traceData_pnr_concentration,
                traceData_pnr_frustration,
                traceData_pnr_surprise,
                traceData_pnr_none_1,
                traceData_pnr_confrustion,
                traceData_pnr_contempt,
                traceData_pnr_dejection,
                traceData_pnr_disgust,
                traceData_pnr_eureka,
                traceData_pnr_pride,
                traceData_pnr_sorrow,
                traceData_pnr_none_2,
            ],
        )

        traceData_self_arousal = GraphTraceDataModel("arousal", data_self_arousal)
        traceData_self_valence = GraphTraceDataModel("valence", data_self_valence)
        traceData_self_cheerful = GraphTraceDataModel(
            "cheerful", data_self_stress_cheerful
        )
        traceData_self_happy = GraphTraceDataModel("happy", data_self_stress_happy)
        traceData_self_angry = GraphTraceDataModel("angry", data_self_stress_angry)
        traceData_self_nervous = GraphTraceDataModel(
            "nervous", data_self_stress_nervous
        )
        traceData_self_sad = GraphTraceDataModel("sad", data_self_stress_sad)
        traceData_self_boredom = GraphTraceDataModel(
            "boredom", data_self_cBROMP_boredom
        )
        traceData_self_confusion = GraphTraceDataModel(
            "confusion", data_self_cBROMP_confusion
        )
        traceData_self_delight = GraphTraceDataModel(
            "delight", data_self_cBROMP_delight
        )
        traceData_self_concentration = GraphTraceDataModel(
            "concentration", data_self_cBROMP_concentration
        )
        traceData_self_frustration = GraphTraceDataModel(
            "frustration", data_self_cBROMP_frustration
        )
        traceData_self_surprise = GraphTraceDataModel(
            "surprise", data_self_cBROMP_surprise
        )
        traceData_self_none_1 = GraphTraceDataModel(
            "commonly used BROMP none", data_self_cBROMP_none_1
        )
        traceData_self_confrustion = GraphTraceDataModel(
            "confrustion", data_self_lcBROMP_confrustion
        )
        traceData_self_contempt = GraphTraceDataModel(
            "contempt", data_self_lcBROMP_contempt
        )
        traceData_self_dejection = GraphTraceDataModel(
            "dejection", data_self_lcBROMP_dejection
        )
        traceData_self_disgust = GraphTraceDataModel(
            "disgust", data_self_lcBROMP_disgust
        )
        traceData_self_eureka = GraphTraceDataModel("eureka", data_self_lcBROMP_eureka)
        traceData_self_pride = GraphTraceDataModel("pride", data_self_lcBROMP_pride)
        traceData_self_sorrow = GraphTraceDataModel("sorrow", data_self_lcBROMP_sorrow)
        traceData_self_none_2 = GraphTraceDataModel(
            "less commonly used BROMP none", data_self_lcBROMP_none_2
        )

        self.plotData_emo_ann_self = GraphPlotDataModel(
            "self emotion annotation",
            [
                traceData_self_arousal,
                traceData_self_valence,
                traceData_self_cheerful,
                traceData_self_happy,
                traceData_self_angry,
                traceData_self_nervous,
                traceData_self_sad,
                traceData_self_boredom,
                traceData_self_confusion,
                traceData_self_delight,
                traceData_self_concentration,
                traceData_self_frustration,
                traceData_self_surprise,
                traceData_self_none_1,
                traceData_self_confrustion,
                traceData_self_contempt,
                traceData_self_dejection,
                traceData_self_disgust,
                traceData_self_eureka,
                traceData_self_pride,
                traceData_self_sorrow,
                traceData_self_none_2,
            ],
        )


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    # view.run_server(debug=True)
    print("skip")
