import numpy as np
import pandas as pd
from models.graphDataModel import GraphPlotDataModel, GraphTraceDataModel
from dataStructure.researchDataType import ResearchDataType


class ResearchDataFactory:
    def __init__(self):
        EMO_ANN_EXTERNAL = pd.read_csv(
            "./dataset/emotion_annotations/aggregated_external_annotations/P5.external.csv"
        )
        EMO_ANN_EXTERNAL = EMO_ANN_EXTERNAL.replace({np.nan: 0, "x": 1})
        EMO_ANN_PARTNER = pd.read_csv(
            "./dataset/emotion_annotations/partner_annotations/P5.partner.csv"
        )
        EMO_ANN_PARTNER = EMO_ANN_PARTNER.replace({np.nan: 0, "x": 1})
        EMO_ANN_SELF = pd.read_csv(
            "./dataset/emotion_annotations/self_annotations/P5.self.csv"
        )
        EMO_ANN_SELF = EMO_ANN_SELF.replace({np.nan: 0, "x": 1})

        E4_ACC = pd.read_csv("./dataset/e4_data/5/E4_ACC.csv")
        E4_ACC["dt_timestamp"] = pd.to_datetime(E4_ACC["timestamp"], unit="ms")
        E4_BVP = pd.read_csv("./dataset/e4_data/5/E4_BVP.csv")
        E4_BVP["dt_timestamp"] = pd.to_datetime(E4_BVP["timestamp"], unit="ms")
        E4_EDA = pd.read_csv("./dataset/e4_data/5/E4_EDA.csv")
        E4_EDA["dt_timestamp"] = pd.to_datetime(E4_EDA["timestamp"], unit="ms")
        E4_HR = pd.read_csv("./dataset/e4_data/5/E4_HR.csv")
        E4_HR["dt_timestamp"] = pd.to_datetime(E4_HR["timestamp"], unit="ms")
        E4_IBI = pd.read_csv("./dataset/e4_data/5/E4_IBI.csv")
        E4_IBI["dt_timestamp"] = pd.to_datetime(E4_IBI["timestamp"], unit="ms")
        E4_TEMP = pd.read_csv("./dataset/e4_data/5/E4_TEMP.csv")
        E4_TEMP["dt_timestamp"] = pd.to_datetime(E4_TEMP["timestamp"], unit="ms")

        ATTENTION = pd.read_csv("./dataset/neurosky_polar_data/5/Attention.csv")
        ATTENTION["dt_timestamp"] = pd.to_datetime(ATTENTION["timestamp"], unit="ms")
        BRAINWAVE = pd.read_csv("./dataset/neurosky_polar_data/5/BrainWave.csv")
        BRAINWAVE["dt_timestamp"] = pd.to_datetime(BRAINWAVE["timestamp"], unit="ms")
        MEDITATION = pd.read_csv("./dataset/neurosky_polar_data/5/Meditation.csv")
        MEDITATION["dt_timestamp"] = pd.to_datetime(MEDITATION["timestamp"], unit="ms")
        POLAR_HR = pd.read_csv("./dataset/neurosky_polar_data/5/Polar_HR.csv")
        POLAR_HR["dt_timestamp"] = pd.to_datetime(POLAR_HR["timestamp"], unit="ms")

        min = POLAR_HR["dt_timestamp"].iat[0]
        max = pd.to_datetime(POLAR_HR["timestamp"].iat[0] + 688000, unit="ms")

        E4_ACC = E4_ACC.loc[
            (E4_ACC["dt_timestamp"] >= min) & (E4_ACC["dt_timestamp"] <= max)
        ].reset_index(drop=False)
        E4_BVP = E4_BVP.loc[
            (E4_BVP["dt_timestamp"] >= min) & (E4_BVP["dt_timestamp"] <= max)
        ].reset_index(drop=False)
        E4_EDA = E4_EDA.loc[
            (E4_EDA["dt_timestamp"] >= min) & (E4_EDA["dt_timestamp"] <= max)
        ].reset_index(drop=False)
        E4_HR = E4_HR.loc[
            (E4_HR["dt_timestamp"] >= min) & (E4_HR["dt_timestamp"] <= max)
        ].reset_index(drop=False)
        E4_IBI = E4_IBI.loc[
            (E4_IBI["dt_timestamp"] >= min) & (E4_IBI["dt_timestamp"] <= max)
        ].reset_index(drop=False)
        E4_TEMP = E4_TEMP.loc[
            (E4_TEMP["dt_timestamp"] >= min) & (E4_TEMP["dt_timestamp"] <= max)
        ].reset_index(drop=False)
        ATTENTION = ATTENTION.loc[
            (ATTENTION["dt_timestamp"] >= min) & (ATTENTION["dt_timestamp"] <= max)
        ].reset_index(drop=False)
        BRAINWAVE = BRAINWAVE.loc[
            (BRAINWAVE["dt_timestamp"] >= min) & (BRAINWAVE["dt_timestamp"] <= max)
        ].reset_index(drop=False)
        MEDITATION = MEDITATION.loc[
            (MEDITATION["dt_timestamp"] >= min) & (MEDITATION["dt_timestamp"] <= max)
        ].reset_index(drop=False)
        POLAR_HR = POLAR_HR.loc[
            (POLAR_HR["dt_timestamp"] >= min) & (POLAR_HR["dt_timestamp"] <= max)
        ].reset_index(drop=False)

        basetimestamp = E4_ACC["timestamp"][0]
        EMO_ANN_EXTERNAL["timestamp"] = (
            EMO_ANN_EXTERNAL["seconds"]
            .astype(int)
            .apply(lambda x: x * 1000 + basetimestamp)
        )
        EMO_ANN_EXTERNAL["dt_timestamp"] = pd.to_datetime(
            EMO_ANN_EXTERNAL["timestamp"], unit="ms"
        )

        EMO_ANN_PARTNER["timestamp"] = (
            EMO_ANN_PARTNER["seconds"]
            .astype(int)
            .apply(lambda x: x * 1000 + basetimestamp)
        )
        EMO_ANN_PARTNER["dt_timestamp"] = pd.to_datetime(
            EMO_ANN_PARTNER["timestamp"], unit="ms"
        )

        EMO_ANN_SELF["timestamp"] = (
            EMO_ANN_SELF["seconds"]
            .astype(int)
            .apply(lambda x: x * 1000 + basetimestamp)
        )
        EMO_ANN_SELF["dt_timestamp"] = pd.to_datetime(
            EMO_ANN_SELF["timestamp"], unit="ms"
        )
        EMO_ANN_EXTERNAL = EMO_ANN_EXTERNAL.loc[
            (EMO_ANN_EXTERNAL["dt_timestamp"] >= min)
            & (EMO_ANN_EXTERNAL["dt_timestamp"] <= max)
        ].reset_index(drop=False)
        EMO_ANN_PARTNER = EMO_ANN_PARTNER.loc[
            (EMO_ANN_PARTNER["dt_timestamp"] >= min)
            & (EMO_ANN_PARTNER["dt_timestamp"] <= max)
        ].reset_index(drop=False)
        EMO_ANN_SELF = EMO_ANN_SELF.loc[
            (EMO_ANN_SELF["dt_timestamp"] >= min)
            & (EMO_ANN_SELF["dt_timestamp"] <= max)
        ].reset_index(drop=False)

        # E4_ACC['ms_timestamp'] = pd.to_datetime(E4_ACC['timestamp']).dt.strftime("%M:%S")
        traceData_acc_x = GraphTraceDataModel("timestamp", "x", "x axis")
        traceData_acc_y = GraphTraceDataModel("timestamp", "y", "y axis")
        traceData_acc_z = GraphTraceDataModel("timestamp", "z", "z axis")
        self.plotData_acc = GraphPlotDataModel(
            "3 axis acceleration (g)",
            ResearchDataType.ACC,
            E4_ACC,
            [traceData_acc_x, traceData_acc_y, traceData_acc_z],
        )

        traceData_bvp = GraphTraceDataModel("timestamp", "value", "BVP")
        self.plotData_bvp = GraphPlotDataModel(
            "BVP (PPG)", ResearchDataType.BVP, E4_BVP, [traceData_bvp]
        )

        traceData_eda = GraphTraceDataModel("timestamp", "value", "EDA")
        self.plotData_eda = GraphPlotDataModel(
            "EDA (uS)", ResearchDataType.EDA, E4_EDA, [traceData_eda]
        )

        HR_DF = E4_HR.copy()
        HR_DF["e4"] = E4_HR["value"]
        HR_DF["ecg"] = POLAR_HR["value"]
        traceData_hr_e4 = GraphTraceDataModel("timestamp", "e4", "E4")
        traceData_hr_ecg = GraphTraceDataModel("timestamp", "ecg", "ECG")
        self.plotData_hr = GraphPlotDataModel(
            "Heart Rate",
            ResearchDataType.HEARTRATE,
            HR_DF,
            [traceData_hr_e4, traceData_hr_ecg],
        )

        traceData_ibi = GraphTraceDataModel("timestamp", "value", "IBI")
        self.plotData_ibi = GraphPlotDataModel(
            "IBI", ResearchDataType.IBI, E4_IBI, [traceData_ibi]
        )

        traceData_temp = GraphTraceDataModel("timestamp", "value", "℃")
        self.plotData_temp = GraphPlotDataModel(
            "Temperature (℃)", ResearchDataType.TEMPERATURE, E4_TEMP, [traceData_temp]
        )

        traceData_bw_high_alpha = GraphTraceDataModel(
            "timestamp", "highAlpha", "high-alpha"
        )
        traceData_bw_high_beta = GraphTraceDataModel(
            "timestamp", "highBeta", "high-beta"
        )
        traceData_bw_middle_gamma = GraphTraceDataModel(
            "timestamp", "middleGamma", "middle-gamma"
        )
        traceData_bw_low_alpha = GraphTraceDataModel(
            "timestamp", "lowAlpha", "low-alpha"
        )
        traceData_bw_low_beta = GraphTraceDataModel("timestamp", "lowBeta", "low-beta")
        traceData_bw_low_gamma = GraphTraceDataModel(
            "timestamp",
            "lowGamma",
            "low-gamma",
        )
        traceData_bw_delta = GraphTraceDataModel("timestamp", "delta", "delta")
        traceData_bw_theta = GraphTraceDataModel("timestamp", "theta", "theta")
        self.plotData_bw = GraphPlotDataModel(
            "Brainwave (relative power)",
            ResearchDataType.BRAINWAVE,
            BRAINWAVE,
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

        ATME_DF = ATTENTION.copy()
        ATME_DF["at"] = ATTENTION["value"]
        ATME_DF["me"] = MEDITATION["value"]
        traceData_att = GraphTraceDataModel("timestamp", "at", "attention")
        traceData_med = GraphTraceDataModel("timestamp", "me", "meditation")
        self.plotData_etc = GraphPlotDataModel(
            "attention & meditation",
            ResearchDataType.ATTENTION_AND_MEDITATION,
            ATME_DF,
            [traceData_att, traceData_med],
        )

        traceData_ext_arousal = GraphTraceDataModel("timestamp", "arousal", "arousal")
        traceData_ext_valence = GraphTraceDataModel("timestamp", "valence", "valence")
        traceData_ext_cheerful = GraphTraceDataModel(
            "timestamp", "cheerful", "cheerful"
        )
        traceData_ext_happy = GraphTraceDataModel("timestamp", "happy", "happy")
        traceData_ext_angry = GraphTraceDataModel("timestamp", "angry", "angry")
        traceData_ext_nervous = GraphTraceDataModel("timestamp", "nervous", "nervous")
        traceData_ext_sad = GraphTraceDataModel("timestamp", "sad", "sad")
        traceData_ext_boredom = GraphTraceDataModel("timestamp", "boredom", "boredom")
        traceData_ext_confusion = GraphTraceDataModel(
            "timestamp", "confusion", "confusion"
        )
        traceData_ext_delight = GraphTraceDataModel("timestamp", "delight", "delight")
        traceData_ext_concentration = GraphTraceDataModel(
            "timestamp", "concentration", "concentration"
        )
        traceData_ext_frustration = GraphTraceDataModel(
            "timestamp", "frustration", "frustration"
        )
        traceData_ext_surprise = GraphTraceDataModel(
            "timestamp", "surprise", "surprise"
        )
        traceData_ext_none_1 = GraphTraceDataModel(
            "timestamp", "none_1", "commonly used BROMP none"
        )
        traceData_ext_confrustion = GraphTraceDataModel(
            "timestamp", "confrustion", "confrustion"
        )
        traceData_ext_contempt = GraphTraceDataModel(
            "timestamp", "contempt", "contempt"
        )
        traceData_ext_dejection = GraphTraceDataModel(
            "timestamp", "dejection", "dejection"
        )
        traceData_ext_disgust = GraphTraceDataModel("timestamp", "disgust", "disgust")
        traceData_ext_eureka = GraphTraceDataModel("timestamp", "eureka", "eureka")
        traceData_ext_pride = GraphTraceDataModel("timestamp", "pride", "pride")
        traceData_ext_sorrow = GraphTraceDataModel("timestamp", "sorrow", "sorrow")
        traceData_ext_none_2 = GraphTraceDataModel(
            "timestamp", "none_2", "less commonly used BROMP none"
        )

        self.plotData_emo_ann_ext_av = GraphPlotDataModel(
            "arousal & valence (ext)",
            ResearchDataType.AROUSAL_AND_VALENCE_EXT,
            EMO_ANN_EXTERNAL,
            [traceData_ext_arousal, traceData_ext_valence],
        )

        self.plotData_emo_ann_ext_stress = GraphPlotDataModel(
            "stress (ext)",
            ResearchDataType.STRESS_EXT,
            EMO_ANN_EXTERNAL,
            [
                traceData_ext_cheerful,
                traceData_ext_happy,
                traceData_ext_angry,
                traceData_ext_nervous,
                traceData_ext_sad,
            ],
        )

        self.plotData_emo_ann_ext_cBROMP = GraphPlotDataModel(
            "educational 1 (e)",
            ResearchDataType.C_BROMP_EXT,
            EMO_ANN_EXTERNAL,
            [
                traceData_ext_boredom,
                traceData_ext_confusion,
                traceData_ext_delight,
                traceData_ext_concentration,
                traceData_ext_frustration,
                traceData_ext_surprise,
                traceData_ext_none_1,
            ],
        )

        self.plotData_emo_ann_ext_lcBROMP = GraphPlotDataModel(
            "educational 2 (e)",
            ResearchDataType.LC_BROMP_EXT,
            EMO_ANN_EXTERNAL,
            [
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

        traceData_pnr_arousal = GraphTraceDataModel("timestamp", "arousal", "arousal")
        traceData_pnr_valence = GraphTraceDataModel("timestamp", "valence", "valence")
        traceData_pnr_cheerful = GraphTraceDataModel(
            "timestamp", "cheerful", "cheerful"
        )
        traceData_pnr_happy = GraphTraceDataModel("timestamp", "happy", "happy")
        traceData_pnr_angry = GraphTraceDataModel("timestamp", "angry", "angry")
        traceData_pnr_nervous = GraphTraceDataModel("timestamp", "nervous", "nervous")
        traceData_pnr_sad = GraphTraceDataModel("timestamp", "sad", "sad")
        traceData_pnr_boredom = GraphTraceDataModel("timestamp", "boredom", "boredom")
        traceData_pnr_confusion = GraphTraceDataModel(
            "timestamp", "confusion", "confusion"
        )
        traceData_pnr_delight = GraphTraceDataModel("timestamp", "delight", "delight")
        traceData_pnr_concentration = GraphTraceDataModel(
            "timestamp", "concentration", "concentration"
        )
        traceData_pnr_frustration = GraphTraceDataModel(
            "timestamp", "frustration", "frustration"
        )
        traceData_pnr_surprise = GraphTraceDataModel(
            "timestamp", "surprise", "surprise"
        )
        traceData_pnr_none_1 = GraphTraceDataModel(
            "timestamp", "none_1", "commonly used BROMP none"
        )
        traceData_pnr_confrustion = GraphTraceDataModel(
            "timestamp", "confrustion", "confrustion"
        )
        traceData_pnr_contempt = GraphTraceDataModel(
            "timestamp", "contempt", "contempt"
        )
        traceData_pnr_dejection = GraphTraceDataModel(
            "timestamp", "dejection", "dejection"
        )
        traceData_pnr_disgust = GraphTraceDataModel("timestamp", "disgust", "disgust")
        traceData_pnr_eureka = GraphTraceDataModel("timestamp", "eureka", "eureka")
        traceData_pnr_pride = GraphTraceDataModel("timestamp", "pride", "pride")
        traceData_pnr_sorrow = GraphTraceDataModel("timestamp", "sorrow", "sorrow")
        traceData_pnr_none_2 = GraphTraceDataModel(
            "timestamp", "none_2", "less commonly used BROMP none"
        )

        self.plotData_emo_ann_pnr_av = GraphPlotDataModel(
            "arousal & valence (pnr)",
            ResearchDataType.AROUSAL_AND_VALENCE_PNR,
            EMO_ANN_PARTNER,
            [traceData_pnr_arousal, traceData_pnr_valence],
        )

        self.plotData_emo_ann_pnr_stress = GraphPlotDataModel(
            "stress (pnr)",
            ResearchDataType.STRESS_PNR,
            EMO_ANN_PARTNER,
            [
                traceData_pnr_cheerful,
                traceData_pnr_happy,
                traceData_pnr_angry,
                traceData_pnr_nervous,
                traceData_pnr_sad,
            ],
        )

        self.plotData_emo_ann_pnr_cBROMP = GraphPlotDataModel(
            "educational 1 (p)",
            ResearchDataType.C_BROMP_PNR,
            EMO_ANN_PARTNER,
            [
                traceData_pnr_boredom,
                traceData_pnr_confusion,
                traceData_pnr_delight,
                traceData_pnr_concentration,
                traceData_pnr_frustration,
                traceData_pnr_surprise,
                traceData_pnr_none_1,
            ],
        )

        self.plotData_emo_ann_pnr_lcBROMP = GraphPlotDataModel(
            "educational 2 (p)",
            ResearchDataType.LC_BROMP_PNR,
            EMO_ANN_PARTNER,
            [
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

        traceData_self_arousal = GraphTraceDataModel("timestamp", "arousal", "arousal")
        traceData_self_valence = GraphTraceDataModel("timestamp", "valence", "valence")
        traceData_self_cheerful = GraphTraceDataModel(
            "timestamp", "cheerful", "cheerful"
        )
        traceData_self_happy = GraphTraceDataModel("timestamp", "happy", "happy")
        traceData_self_angry = GraphTraceDataModel("timestamp", "angry", "angry")
        traceData_self_nervous = GraphTraceDataModel("timestamp", "nervous", "nervous")
        traceData_self_sad = GraphTraceDataModel("timestamp", "sad", "sad")
        traceData_self_boredom = GraphTraceDataModel("timestamp", "boredom", "boredom")
        traceData_self_confusion = GraphTraceDataModel(
            "timestamp", "confusion", "confusion"
        )
        traceData_self_delight = GraphTraceDataModel("timestamp", "delight", "delight")
        traceData_self_concentration = GraphTraceDataModel(
            "timestamp", "concentration", "concentration"
        )
        traceData_self_frustration = GraphTraceDataModel(
            "timestamp", "frustration", "frustration"
        )
        traceData_self_surprise = GraphTraceDataModel(
            "timestamp", "surprise", "surprise"
        )
        traceData_self_none_1 = GraphTraceDataModel(
            "timestamp", "none_1", "commonly used BROMP none"
        )
        traceData_self_confrustion = GraphTraceDataModel(
            "timestamp", "confrustion", "confrustion"
        )
        traceData_self_contempt = GraphTraceDataModel(
            "timestamp", "contempt", "contempt"
        )
        traceData_self_dejection = GraphTraceDataModel(
            "timestamp", "dejection", "dejection"
        )
        traceData_self_disgust = GraphTraceDataModel("timestamp", "disgust", "disgust")
        traceData_self_eureka = GraphTraceDataModel("timestamp", "eureka", "eureka")
        traceData_self_pride = GraphTraceDataModel("timestamp", "pride", "pride")
        traceData_self_sorrow = GraphTraceDataModel("timestamp", "sorrow", "sorrow")
        traceData_self_none_2 = GraphTraceDataModel(
            "timestamp", "none_2", "less commonly used BROMP none"
        )

        self.plotData_emo_ann_self_av = GraphPlotDataModel(
            "arousal & valence (self)",
            ResearchDataType.AROUSAL_AND_VALENCE_SELF,
            EMO_ANN_SELF,
            [traceData_self_arousal, traceData_self_valence],
        )

        self.plotData_emo_ann_self_stress = GraphPlotDataModel(
            "stress (self)",
            ResearchDataType.STRESS_SELF,
            EMO_ANN_SELF,
            [
                traceData_self_cheerful,
                traceData_self_happy,
                traceData_self_angry,
                traceData_self_nervous,
                traceData_self_sad,
            ],
        )

        self.plotData_emo_ann_self_cBROMP = GraphPlotDataModel(
            "educational 1 (s)",
            ResearchDataType.C_BROMP_SELF,
            EMO_ANN_SELF,
            [
                traceData_self_boredom,
                traceData_self_confusion,
                traceData_self_delight,
                traceData_self_concentration,
                traceData_self_frustration,
                traceData_self_surprise,
                traceData_self_none_1,
            ],
        )

        self.plotData_emo_ann_self_lcBROMP = GraphPlotDataModel(
            "educational 2 (s)",
            ResearchDataType.LC_BROMP_SELF,
            EMO_ANN_SELF,
            [
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
